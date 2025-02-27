from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6]]
    palindromes = set()
    for p in permutations(letters, 4):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes