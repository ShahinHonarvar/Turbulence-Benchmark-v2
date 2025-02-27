from itertools import permutations

def palindromes_between_indices(str1):
    str1 = str1.lower()
    set1 = set()
    for i in permutations(str1[3:10]):
        g = ''.join(i)
        if g == g[::-1] and len(g) >= 5:
            set1.add(g)
    if len(set.intersection(set1)) == 0:
        return set()
    else:
        return set.intersection(set1)