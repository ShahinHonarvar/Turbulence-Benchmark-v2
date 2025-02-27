from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3:
                    c1 = Counter(lst[i].lower())
                    c2 = Counter(lst[j].lower())
                    if c1 == c2:
                        count += 1
    if count <= 14:
        return True
    return False