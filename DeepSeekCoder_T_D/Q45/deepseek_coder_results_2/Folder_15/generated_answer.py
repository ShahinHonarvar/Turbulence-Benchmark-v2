from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def extract_letters(start, end):
        return ''.join(filter(str.isalpha, s[start:end + 1])).lower()

    def generate_palindromes(letters):
        palindromes = set()
        for i in range(3, len(letters) + 1):
            for perm in permutations(letters, i):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
        return palindromes
    letters = extract_letters(1, 2)
    return generate_palindromes(letters)