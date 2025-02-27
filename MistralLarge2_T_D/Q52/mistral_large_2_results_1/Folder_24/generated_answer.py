def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    n = 29
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring.lower()):
            palindromes.add(substring)
    return palindromes