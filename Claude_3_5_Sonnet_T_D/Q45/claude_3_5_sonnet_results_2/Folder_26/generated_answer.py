from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:7])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        palindromes = set()
        for i in range(3, len(chars) + 1):
            for perm in permutations(chars, i):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
        return palindromes
    return generate_palindromes(letters)