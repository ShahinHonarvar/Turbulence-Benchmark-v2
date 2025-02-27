def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = ''.join(filter(str.isalpha, text)).lower()
    palindromes = set()
    n = 147
    for start in range(len(text)):
        for end in range(start + n, len(text) + 1):
            substr = text[start:end]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes