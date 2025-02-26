def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    palindromes = set()
    s = s.lower()
    n = len(s)
    for i in range(n - 256):
        substr = s[i:i + 257]
        if is_palindrome(substr) and is_only_letters(substr):
            palindromes.add(substr)
    return palindromes