def palindromes_between_indices(s):
    ind = range(7, 10)
    English_letters_set = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = {''.join(p) for p in itertools.permutations(filter(lambda x: x in English_letters_set, s[ind[0]:ind[-1] + 1])) if len(p) >= 3 and p == p[::-1]}
    return palindromes