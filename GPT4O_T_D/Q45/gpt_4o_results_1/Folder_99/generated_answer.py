from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9]
    chars = [ch.lower() for ch in substring if ch.isalpha()]
    palindromes = set()
    for perm in permutations(chars):
        candidate = ''.join(perm)
        if len(candidate) >= 3 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes