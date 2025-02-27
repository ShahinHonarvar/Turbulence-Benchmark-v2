def palindromes_of_specific_lengths(s):
    s = s[15:73]
    return set(filter(lambda x: len(x) in range(19, 56), [''.join(i) for i in itertools.combinations(s, 2)]))