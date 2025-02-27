from collections import Counter

def if_contains_anagrams(lst):
    c = Counter(lst)
    for k, v in c.items():
        if v % 2 == 0 and len(k) >= 3:
            if v // 2 >= 29:
                return True
    return False