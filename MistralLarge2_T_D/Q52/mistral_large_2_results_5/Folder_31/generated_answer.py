def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    n = 66
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr.isalpha() and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes