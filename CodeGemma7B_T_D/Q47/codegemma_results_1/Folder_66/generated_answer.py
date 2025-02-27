def palindromes_of_specific_lengths(text):

    def is_english_palindrome(text):
        return text == text[::-1] and text.isalpha()
    return {substring for substring in text[32:79 + 1] if 35 <= len(substring) <= 41 and is_english_palindrome(substring.casefold())}