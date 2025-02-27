import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[1:7]))
    s = s.lower()
    palindromes = {''.join(i) for i in itertools.permutations(s) if i == i[::-1] and len(i) > 2}
    return palindromes