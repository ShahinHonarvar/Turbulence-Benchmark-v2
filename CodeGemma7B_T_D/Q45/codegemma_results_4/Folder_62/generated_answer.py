from itertools import permutations

def palindromes_between_indices(text):
    """
    :type text: str
    """
    text = text.lower()
    d = {}
    for i in range(9):
        for j in range(i, 9):
            d[text[i:j + 1]] = True
    return {''.join(p) for p in permutations(text) if p in d}