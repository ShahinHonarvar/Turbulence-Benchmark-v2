from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:6])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, min_length):
        palindromes = set()
        for i in range(min_length, len(chars) + 1):
            for perm in permutations(chars, i):
                word = ''.join(perm)
                if is_palindrome(word) and len(word) >= min_length:
                    palindromes.add(word)
        return palindromes
    return generate_palindromes(letters, 5)