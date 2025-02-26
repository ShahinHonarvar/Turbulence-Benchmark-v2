from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes