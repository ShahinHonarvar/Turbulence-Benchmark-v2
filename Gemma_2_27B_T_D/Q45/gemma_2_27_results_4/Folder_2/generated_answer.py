from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word[::-1] == word and len(word) >= 6:
            palindromes.add(word)
    return palindromes