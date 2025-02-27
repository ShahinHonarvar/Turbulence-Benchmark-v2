from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    if len(s) < 5:
        return set()
    letters = ''.join((c.lower() for c in s[2:5] if c.isalpha()))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes