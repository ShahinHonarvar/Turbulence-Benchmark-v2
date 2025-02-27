from itertools import permutations

def palindromes_between_indices(text):
    letters = text[5:8]
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p).lower()
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes