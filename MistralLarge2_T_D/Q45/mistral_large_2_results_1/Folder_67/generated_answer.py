from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:7].lower() if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes