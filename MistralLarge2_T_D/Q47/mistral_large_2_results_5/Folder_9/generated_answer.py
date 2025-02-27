def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    n = len(s)
    s = s[:301].lower()
    for length in range(50, 61):
        for i in range(301 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes