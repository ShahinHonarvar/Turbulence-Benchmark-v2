from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    characters = [c for c in s if c.isalpha()]
    unique_palindromes = set()
    for i in range(5, len(characters) + 1):
        for p in permutations(characters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                unique_palindromes.add(candidate)
    return unique_palindromes