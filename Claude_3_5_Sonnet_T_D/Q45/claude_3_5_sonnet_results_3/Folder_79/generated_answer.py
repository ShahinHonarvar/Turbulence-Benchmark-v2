from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:8] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 3
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes