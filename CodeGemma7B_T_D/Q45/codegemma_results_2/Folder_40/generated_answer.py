def palindromes_between_indices(str_in):
    test_string = str_in[4:10]
    if len(test_string) < 7:
        return set()
    s = set()
    for permutation in itertools.permutations(test_string):
        word = ''.join(permutation)
        if word == word[::-1]:
            s.add(word)
    return s