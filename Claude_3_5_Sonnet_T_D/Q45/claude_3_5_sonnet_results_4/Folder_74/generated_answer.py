from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:7])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, min_length):
        palindromes = set()
        for i in range(min_length, len(chars) + 1):
            for perm in permutations(chars, i):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
        return palindromes
    return generate_palindromes(letters, 6)