from collections import Counter

def if_contains_anagrams(strings):
    count_anagrams = 0
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            if Counter(strings[i].lower()) == Counter(strings[j].lower()):
                count_anagrams += 1
            if count_anagrams > 46:
                return False
    return count_anagrams <= 46