def palindrome_of_length_n(s):

    def is_palindrome(w):
        return w == w[::-1]
    n = 401
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes