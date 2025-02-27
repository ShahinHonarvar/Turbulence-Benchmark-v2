from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:8]
    palindromes = set()
    for p in permutations(filter(str.isalpha, letters)):
        candidate = ''.join(p).lower()
        if candidate == candidate[::-1] and len(candidate) >= 7:
            palindromes.add(candidate)
    return palindromes