from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((ch for ch in s[7:10] if ch.isalpha())).lower()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes