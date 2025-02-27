from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[4:9] if c.isalpha()))
    if len(letters) < 3:
        return set()
    palindromes = set()
    for p in permutations(letters, len(letters) // 2 + len(letters) % 2):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes