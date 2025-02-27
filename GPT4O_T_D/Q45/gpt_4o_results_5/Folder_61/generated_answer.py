from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:8].lower()
    filtered_substring = ''.join([ch for ch in substring if ch.isalpha()])
    perm = set(permutations(filtered_substring, len(filtered_substring)))
    palindromes = {''.join(p) for p in perm if ''.join(p) == ''.join(p)[::-1] and len(''.join(p)) >= 7}
    return palindromes