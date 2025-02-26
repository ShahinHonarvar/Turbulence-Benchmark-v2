def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]

    def is_letter_only(s):
        return s.isalpha()
    text = text.lower()
    palindromes = set()
    for length in range(115, len(text) + 1):
        for start in range(len(text) - length + 1):
            substring = text[start:start + length]
            if is_letter_only(substring) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes