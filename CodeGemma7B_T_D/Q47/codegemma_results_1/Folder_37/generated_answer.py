def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]

    def is_english_palindrome(s):
        return s.isalpha() and is_palindrome(s)
    return {word for word in s[0:10].lower().split() if len(word) in (3, 4, 5) and is_english_palindrome(word)}