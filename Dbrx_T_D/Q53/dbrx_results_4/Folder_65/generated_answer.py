def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def find_palindromes_at_least_n(s, n=15):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i:j + 1]) and j + 1 - i >= n:
                palindromes.add(s[i:j + 1])
    return palindromes