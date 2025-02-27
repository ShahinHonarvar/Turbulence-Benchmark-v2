import itertools

def palindromes_between_indices(s):
    letters = s[1:7]
    palindromes = {''.join(p) for p in itertools.permutations(letters) if p == p[::-1]}
    palindromes = {p for p in palindromes if len(p) >= 3}
    return palindromes