from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                l1 = Counter(lst[i].lower())
                l2 = Counter(lst[j].lower())
                if l1 == l2:
                    count += 1
    return count <= 173