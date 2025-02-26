from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            word = ''.join(perm)
            rword = word[::-1]
            if is_palindrome(word) and len(word) >= 4:
                palindromes.add(word)
    return palindromes