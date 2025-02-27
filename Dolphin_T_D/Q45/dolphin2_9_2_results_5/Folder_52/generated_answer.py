import itertools

def palindromes_between_indices(s):
    length = len(s)
    if length < 8:
        return set()
    substring = s[:8]
    palindromes = set()
    for p in itertools.permutations(substring):
        palindromes.update(set(p))
    for word in palindromes:
        if len(word) < 6 or word == word.upper() or word == word.lower():
            palindromes.remove(word)
    return {word.lower() for word in palindromes}