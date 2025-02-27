from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for p in permutations(s):
        candidate = ''.join(p)
        if len(candidate) >= 6 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes