from itertools import permutations

def palindromes_between_indices(s):
    s = s[:4].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p)
        mid = len(candidate) // 2
        if candidate[:mid] == candidate[-1:-mid - 1:-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes