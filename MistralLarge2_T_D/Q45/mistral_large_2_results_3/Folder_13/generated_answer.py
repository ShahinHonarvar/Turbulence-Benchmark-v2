from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[3:10] if c.isalpha())).lower()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes