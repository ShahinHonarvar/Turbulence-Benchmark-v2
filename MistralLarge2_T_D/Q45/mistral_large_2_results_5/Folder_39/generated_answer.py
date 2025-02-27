from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes