from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = [char.lower() for char in s[2:10] if char.isalpha()]
    palindromes = set()
    for length in range(6, len(english_letters) + 1):
        for p in permutations(english_letters, length):
            candidate = ''.join(p)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes