def palindromes_between_indices(s):
    substring = s[1:9].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def permute(letters, prefix=''):
        if len(prefix) >= 4 and is_palindrome(prefix):
            palindromes.add(prefix)
        for i, letter in enumerate(letters):
            permute(letters[:i] + letters[i + 1:], prefix + letter)
    permute(letters)
    return palindromes