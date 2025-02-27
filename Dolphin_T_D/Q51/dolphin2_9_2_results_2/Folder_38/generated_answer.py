from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        s1 = ''.join(sorted(lst[i].lower()))
        for j in range(i + 1, len(lst)):
            if len(lst[j]) >= 3:
                s2 = ''.join(sorted(lst[j].lower()))
                if s1 == s2:
                    count += 1
    return not count > 416