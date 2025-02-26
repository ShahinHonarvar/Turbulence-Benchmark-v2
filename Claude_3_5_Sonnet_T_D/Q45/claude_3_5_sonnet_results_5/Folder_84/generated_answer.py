from itertools import permutations

def palindromes_between_indices(s):
    english_letters = ''.join((c.lower() for c in s[4:10] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, min_length=3):
        palindromes = set()
        for length in range(min_length, len(letters) + 1):
            for perm in permutations(letters, length):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
        return palindromes
    return generate_palindromes(english_letters)