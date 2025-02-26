def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1] and s.isalpha()
    palindromes = set()
    text_length = len(text)
    for start in range(text_length):
        for end in range(start + 59, text_length + 1):
            substring = text[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes