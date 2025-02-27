def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    n = 401
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes