from collections import Counter

def if_contains_anagrams(lst):
    n = len(lst)
    for i in range(n):
        if i >= n:
            break
        count = Counter(lst[i].lower())
        for j in range(i + 1, n):
            if j >= n:
                break
            count -= Counter(lst[j].lower())
            if i >= j:
                break
            if sum(count.values()) in (0, 1) and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                return True
    return False