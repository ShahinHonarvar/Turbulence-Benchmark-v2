from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha()]
    if len(letters) < 5:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm).lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes