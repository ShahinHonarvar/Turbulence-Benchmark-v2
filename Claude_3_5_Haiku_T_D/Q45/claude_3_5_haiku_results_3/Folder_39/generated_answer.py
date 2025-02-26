from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:6] if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for perm_length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, perm_length)):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes