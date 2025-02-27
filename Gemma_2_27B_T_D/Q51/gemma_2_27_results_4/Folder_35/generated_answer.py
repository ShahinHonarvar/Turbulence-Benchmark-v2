from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            a = Counter(strings[i].lower())
            b = Counter(strings[j].lower())
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (a == b):
                count += 1
    return count <= 210