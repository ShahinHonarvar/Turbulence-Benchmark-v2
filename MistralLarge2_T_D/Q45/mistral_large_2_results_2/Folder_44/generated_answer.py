from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[2:8])).lower()
    result = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if is_palindrome(word):
                result.add(word)
    return result