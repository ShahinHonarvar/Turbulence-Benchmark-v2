from collections import Counter

def if_contains_anagrams(lst):
    ans = False
    lst = [i.lower() for i in lst]
    pair_number = set()
    for i in range(len(lst)):
        if len(lst[i]) >= 3 and all((c.isalpha() for c in lst[i])):
            temp = Counter(lst[i])
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3 and all((c.isalpha() for c in lst[j])) and (Counter(lst[j]) == temp):
                    pair_number.add((i, j))
    if len(pair_number) <= 29:
        ans = True
    return ans