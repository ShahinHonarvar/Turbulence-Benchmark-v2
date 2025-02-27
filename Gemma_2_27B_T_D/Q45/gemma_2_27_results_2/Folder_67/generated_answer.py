from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:7].lower()
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            palindromes.add(candidate)
    return palindromes