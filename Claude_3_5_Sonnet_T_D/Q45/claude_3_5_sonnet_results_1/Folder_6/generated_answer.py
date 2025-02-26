from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = ''.join(filter(str.isalpha, s[:8])).lower()
    result = set()
    for i in range(4, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                result.add(word)
    return result