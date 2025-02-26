from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:6] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes