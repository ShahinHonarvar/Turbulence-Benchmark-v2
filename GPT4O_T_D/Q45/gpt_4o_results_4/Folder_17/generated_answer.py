from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7]
    letters = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes