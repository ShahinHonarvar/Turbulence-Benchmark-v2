from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    chars = [c for c in s[1:8] if c.isalpha()]
    palindromes = set()
    for perm in permutations(chars, len(chars)):
        word = ''.join(perm)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    return palindromes