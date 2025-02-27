def palindromes_between_indices(string):
    alplist = list(string[6:9].lower())
    alphalist.sort()
    str1 = ''.join(alphalist)
    set1 = set()
    if len(str1) == 4:
        for i in permutations(alplist, 4):
            i = ''.join(i)
            set1.add(i)
    return set1