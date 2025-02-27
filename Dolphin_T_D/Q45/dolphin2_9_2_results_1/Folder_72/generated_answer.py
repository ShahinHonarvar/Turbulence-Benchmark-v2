import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:8] if c.isalpha()]
    palindromes = set()
    for p in itertools.permutations(letters, 6):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word.lower())
    return palindromes