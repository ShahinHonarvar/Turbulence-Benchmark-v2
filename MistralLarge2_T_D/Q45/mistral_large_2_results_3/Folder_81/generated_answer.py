from itertools import permutations

def palindromes_between_indices(s):
    substr = ''.join((ch for ch in s[:7] if ch.isalpha())).lower()
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for perm in permutations(substr, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes