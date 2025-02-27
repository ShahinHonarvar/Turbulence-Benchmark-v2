def palindrome_of_length_at_least_n(text, min_length=59):

    def is_palindrome(s):
        s = ''.join(filter(str.isalpha, s))
        s = s.lower()
        return s == s[::-1]
    palindromes = set(filter(is_palindrome, (text[i:j] for i in range(len(text)) for j in range(i + 1, len(text) + 1) if j - i >= min_length)))
    return palindromes