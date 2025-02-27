from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[1:8] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p)
        if len(candidate) >= 5 and candidate.lower() == candidate[::-1].lower():
            palindromes.add(candidate)
    return palindromes