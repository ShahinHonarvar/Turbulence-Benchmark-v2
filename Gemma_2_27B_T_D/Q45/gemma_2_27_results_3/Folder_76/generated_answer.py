from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[1:5] if c.isalpha()))
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes