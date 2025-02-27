from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = sorted(lst[i].lower())
            s2 = sorted(lst[j].lower())
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (s1 == s2):
                count += 1
    return count >= 233