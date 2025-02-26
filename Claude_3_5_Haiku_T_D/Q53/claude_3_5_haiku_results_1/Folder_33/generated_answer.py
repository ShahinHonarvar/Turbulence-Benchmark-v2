def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]

    def is_letter_only(s):
        return s.isalpha()
    text = text.lower()
    palindromes = set()
    for length in range(141, len(text) + 1):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if is_palindrome(substring) and is_letter_only(substring):
                palindromes.add(substring)
    return palindromes