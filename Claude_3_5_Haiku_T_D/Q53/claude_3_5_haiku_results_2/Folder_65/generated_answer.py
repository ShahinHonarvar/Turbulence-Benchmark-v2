def palindrome_of_length_at_least_n(s):

    def is_palindrome(x):
        return x == x[::-1]
    s = s.lower()
    palindromes = set()
    for length in range(15, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes