from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[:7].lower()
    letters = [char for char in s if char.isalpha()]
    result = set()
    for i in range(4, len(letters) + 1):
        for perm in set(permutations(letters, i)):
            word = ''.join(perm)
            if is_palindrome(word):
                result.add(word)
    return result