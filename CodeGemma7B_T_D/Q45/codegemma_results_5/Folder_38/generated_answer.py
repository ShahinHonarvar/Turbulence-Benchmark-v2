from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    letters = [c for c in text[3:9] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        if p == p[::-1] and len(p) >= 5:
            palindromes.add(''.join(p))
    return palindromes