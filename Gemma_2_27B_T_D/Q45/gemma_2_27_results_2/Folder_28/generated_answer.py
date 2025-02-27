from itertools import permutations

def palindromes_between_indices(text):
    letters = text[1:6]
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes