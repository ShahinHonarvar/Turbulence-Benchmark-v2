def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    n = 276
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes