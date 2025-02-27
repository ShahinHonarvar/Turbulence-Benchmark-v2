from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    substring = s[7:10]
    filtered_chars = [char for char in substring if char in english_letters]
    filtered_chars = list(map(str.lower, filtered_chars))
    palindromes = set()
    for length in range(4, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes