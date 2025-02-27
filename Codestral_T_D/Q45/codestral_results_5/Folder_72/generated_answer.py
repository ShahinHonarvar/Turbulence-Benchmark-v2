import itertools

def palindromes_between_indices(s):
    substring = s[1:8].lower()
    permutations = set(itertools.permutations(substring, r=None))
    palindromes = {''.join(perm) for perm in permutations if ''.join(perm) == ''.join(perm)[::-1] and len(perm) >= 6}
    return palindromes