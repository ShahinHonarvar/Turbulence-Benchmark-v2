from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[2:9] if c.isalpha()))
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p)
        if len(candidate) >= 6 and candidate.lower() == candidate.lower()[::-1]:
            palindromes.add(candidate)
    return palindromes