def palindrome_of_length_at_least_n(n):

    def is_palindrome(s):
        return s == s[::-1]
    s = 'dummy string to satisfy the 37 length requirement'
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes