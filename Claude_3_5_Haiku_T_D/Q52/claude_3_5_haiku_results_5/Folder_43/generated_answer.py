def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1] and substr.lower().isalpha()
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 50):
        substr = s[i:i + 51]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes