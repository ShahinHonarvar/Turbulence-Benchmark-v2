from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst_of_strings):
    lst = [i.lower() for i in lst_of_strings if len(i) >= 3]
    counter = Counter(lst)
    count = 0
    for i in counter:
        if counter[i] > 1:
            comb = list(combinations(counter.items(), 2))
            for j in comb:
                if j[0][1] > 1 and j[1][1] > 1:
                    count += 1
    if count >= 155:
        return True
    else:
        return False