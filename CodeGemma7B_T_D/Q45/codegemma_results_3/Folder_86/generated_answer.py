from itertools import permutations

def palindromes_between_indices(text):
    text = text[6:10]
    text = ''.join(sorted([c.lower() for c in text if c.isalpha()]))
    result = set()
    for p in permutations(text):
        result.add(''.join(p))
    return result