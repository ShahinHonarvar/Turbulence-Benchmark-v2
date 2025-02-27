from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for k in range(len(strings)):
        for j in range(k + 1, len(strings)):
            if len(strings[k]) < 3 or len(strings[j]) < 3:
                continue
            if Counter(strings[k].lower()) == Counter(strings[j].lower()):
                count += 1
    return count <= 416