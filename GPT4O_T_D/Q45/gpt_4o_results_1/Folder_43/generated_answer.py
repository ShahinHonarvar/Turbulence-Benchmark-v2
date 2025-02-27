from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[2:6].lower()
    english_letters = ''.join(filter(str.isalpha, substring))
    potential_words = set([''.join(p) for p in permutations(english_letters) if len(p) >= 4])
    palindromes = {word for word in potential_words if is_palindrome(word)}
    return palindromes