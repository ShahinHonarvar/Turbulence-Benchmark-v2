from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 3

    def generate_palindromes(chars):
        result = set()
        for i in range(3, len(chars) + 1):
            for perm in permutations(chars, i):
                word = ''.join(perm)
                if is_palindrome(word):
                    result.add(word)
        return result
    return generate_palindromes(letters)