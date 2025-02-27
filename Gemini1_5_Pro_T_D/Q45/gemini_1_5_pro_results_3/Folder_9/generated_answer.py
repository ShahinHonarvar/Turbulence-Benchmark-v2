from itertools import permutations

def palindromes_between_indices(s):
    letters = set([c for c in s[0:7] if c.isalpha()])
    if len(letters) < 7:
        return set()
    result = set()
    for p in permutations(letters, 7):
        word = ''.join(p)
        if word.lower() == word[::-1].lower():
            result.add(word.lower())
    return result