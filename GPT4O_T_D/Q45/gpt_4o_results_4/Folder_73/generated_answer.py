from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = s[3:7].lower()
    letters = [char for char in substr if char.isalpha()]
    result = set()
    if len(letters) < 3:
        return result
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                result.add(word)
    return result