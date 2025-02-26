from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[2:10] if char.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, min_length):
        result = set()
        for i in range(min_length, len(chars) + 1):
            for perm in permutations(chars, i):
                word = ''.join(perm)
                if is_palindrome(word):
                    result.add(word)
        return result
    return generate_palindromes(letters, 7)