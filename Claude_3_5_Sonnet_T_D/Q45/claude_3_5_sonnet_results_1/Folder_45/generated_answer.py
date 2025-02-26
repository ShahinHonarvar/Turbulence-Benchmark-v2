from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[5:10] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, min_length):
        palindromes = set()
        for length in range(min_length, len(chars) + 1):
            for perm in permutations(chars, length):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
        return palindromes
    return generate_palindromes(letters, 4)