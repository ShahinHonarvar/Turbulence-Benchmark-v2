def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = ''.join(filter(str.isalpha, text)).lower()
    n = len(text)
    palindromes = set()
    for start in range(n):
        for end in range(start + 31, n + 1):
            if is_palindrome(text[start:end]):
                palindromes.add(text[start:end])
    return palindromes