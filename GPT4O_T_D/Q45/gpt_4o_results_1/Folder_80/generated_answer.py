from itertools import permutations

def palindromes_between_indices(s):
    substring_letters = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()
    for perm in set(permutations(substring_letters)):
        word = ''.join(perm)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    return palindromes