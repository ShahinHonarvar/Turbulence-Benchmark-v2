from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes