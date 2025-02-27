from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[4:10] if c.isalpha())).lower()
    all_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                all_palindromes.add(word)
    return all_palindromes