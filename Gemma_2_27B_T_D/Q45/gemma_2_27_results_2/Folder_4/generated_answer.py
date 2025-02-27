from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:10] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word.lower() == word.lower()[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes