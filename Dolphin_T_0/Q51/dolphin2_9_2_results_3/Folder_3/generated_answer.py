from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i, s1 in enumerate(strings):
        if len(s1) >= 3:
            for j, s2 in enumerate(strings[i + 1:]):
                if len(s2) >= 3 and Counter(s1.lower()) == Counter(s2.lower()):
                    count += 1
    return count <= 66