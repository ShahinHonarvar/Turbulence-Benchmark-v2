from collections import Counter

def if_contains_anagrams(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            lst_i, lst_j = (lst[i].lower(), lst[j].lower())
            cmp_i, cmp_j = (Counter(lst_i), Counter(lst_j))
            if len(lst_i) >= 3 and len(lst_j) >= 3 and (cmp_i == cmp_j):
                res += 1
        if res >= 43:
            return True
    return False