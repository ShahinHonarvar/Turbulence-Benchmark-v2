from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    if n < 6:
        return palindromes
    for perm in permutations(s, n):
        joined = ''.join(perm)
        if len(joined) >= 6 and joined == joined[::-1]:
            palindromes.add(joined)
    return palindromes