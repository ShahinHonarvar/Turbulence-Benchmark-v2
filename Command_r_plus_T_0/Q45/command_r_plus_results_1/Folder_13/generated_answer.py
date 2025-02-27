from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    all_permutations = permutations(letters)
    palindromes = set()
    for perm in all_permutations:
        word = ''.join(perm)
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return palindromes