from itertools import combinations_with_replacement

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[4:9].lower())
    palindromes = set()
    for letter in letters:
        for combo in combinations_with_replacement(letters, 5):
            word = ''.join(combo)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes