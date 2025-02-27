def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for length in range(40, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes