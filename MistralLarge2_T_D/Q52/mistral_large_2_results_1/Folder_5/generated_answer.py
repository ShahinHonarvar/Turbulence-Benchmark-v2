def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    n = 17
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr.isalpha() and is_palindrome(substr):
            palindromes.add(substr.lower())
    return palindromes