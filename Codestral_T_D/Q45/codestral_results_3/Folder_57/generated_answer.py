from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    palindromes = set()
    for perm in permutations(s, len(s)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes