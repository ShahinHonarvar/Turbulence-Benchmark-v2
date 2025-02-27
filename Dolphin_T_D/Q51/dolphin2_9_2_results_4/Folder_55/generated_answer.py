from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (strings[i].lower() != strings[j].lower()):
                counter1 = Counter(strings[i].lower())
                counter2 = Counter(strings[j].lower())
                if counter1 == counter2:
                    count += 1
    return count <= 44