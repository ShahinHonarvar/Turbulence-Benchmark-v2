import string
    from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[2:6] if c in string.ascii_lowercase]
    palindromes = set()
    for p in permutations(letters, 5):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes