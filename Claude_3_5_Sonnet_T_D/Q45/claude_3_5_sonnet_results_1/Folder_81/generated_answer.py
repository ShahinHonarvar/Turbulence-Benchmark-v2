import itertools

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[:7] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, min_length):
        result = set()
        for length in range(min_length, len(chars) + 1):
            for perm in itertools.permutations(chars, length):
                word = ''.join(perm)
                if is_palindrome(word):
                    result.add(word)
        return result
    return generate_palindromes(letters, 3)