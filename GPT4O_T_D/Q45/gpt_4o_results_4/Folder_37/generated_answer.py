from itertools import permutations

def palindromes_between_indices(s):
    substr = s[1:5].lower()
    letters = ''.join(filter(str.isalpha, substr))
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(letters, len(letters))):
        word = ''.join(perm)
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return set(filter(lambda x: len(x) >= 5, palindromes))