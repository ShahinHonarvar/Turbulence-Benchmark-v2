from itertools import permutations

def palindromes_between_indices(input_string):
    letters = ''.join((char.lower() for char in input_string[4:10] if char.isalpha()))

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(chars, min_length):
        result = set()
        for length in range(min_length, len(chars) + 1):
            for perm in permutations(chars, length):
                word = ''.join(perm)
                if is_palindrome(word):
                    result.add(word)
        return result
    return generate_palindromes(letters, 6)