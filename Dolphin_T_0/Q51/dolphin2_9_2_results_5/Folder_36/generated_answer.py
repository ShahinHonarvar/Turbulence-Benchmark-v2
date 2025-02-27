from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    pairs = 0
    count = Counter((i.lower() for i in lst if len(i) >= 3))
    for i in count:
        for j in permutations(i):
            if ''.join(j) in count:
                if i != ''.join(j):
                    pairs += 1
                    break
    if pairs <= 25:
        return True
    else:
        return False