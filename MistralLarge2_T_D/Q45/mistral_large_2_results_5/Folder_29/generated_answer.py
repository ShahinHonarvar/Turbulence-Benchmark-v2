from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    indices_range = s[2:10]
    english_letters = ''.join(filter(str.isalpha, indices_range)).lower()
    if len(english_letters) < 6:
        return set()
    palindromes = set()
    for length in range(6, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes