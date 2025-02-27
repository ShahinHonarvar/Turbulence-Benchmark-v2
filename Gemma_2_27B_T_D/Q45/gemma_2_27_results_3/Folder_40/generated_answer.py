from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:10] if c.isalpha())).lower()
    palindromes = set()
    for permutation in permutations(letters):
        candidate = ''.join(permutation)
        if len(candidate) >= 7 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes