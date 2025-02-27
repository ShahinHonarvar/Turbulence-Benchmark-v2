import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[3:9])).lower()
    return set(filter(lambda x: len(x) >= 5, (''.join(i) for i in itertools.permutations(s) if i == i[::-1])))