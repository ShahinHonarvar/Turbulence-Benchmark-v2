from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            str1_counter = Counter(strings[i].lower())
            str2_counter = Counter(strings[j].lower())
            if str1_counter == str2_counter:
                count += 1
    return count <= 147