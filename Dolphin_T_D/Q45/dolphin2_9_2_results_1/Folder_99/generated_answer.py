from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9]
    palindromes = set()
    for p in permutations(substring, len(substring)):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes