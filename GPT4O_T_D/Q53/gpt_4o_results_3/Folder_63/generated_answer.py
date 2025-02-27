def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    min_length = 37
    for i in range(n):
        for j in range(i + min_length, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes