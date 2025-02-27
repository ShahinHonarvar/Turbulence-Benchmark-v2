def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    n = 67
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - n + 1):
        if is_palindrome(s[i:i + n]):
            palindromes.add(s[i:i + n])
    return palindromes