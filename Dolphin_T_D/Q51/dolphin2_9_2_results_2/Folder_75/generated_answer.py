from collections import Counter
    from math import factorial

def if_contains_anagrams(lst):
    lst = [Counter(s.lower()) for s in lst if len(s) >= 3]
    count = True
    for i in range(len(lst)):
        if count:
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j]:
                    if i != j:
                        pairs = factorial(len(lst[i])) / factorial(len(lst[i]) - 2) / 2
                        if pairs > 55:
                            return True
                        if pairs == 55:
                            return False
    return False