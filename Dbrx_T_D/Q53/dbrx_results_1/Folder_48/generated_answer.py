def is_palindrome(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return s == s[::-1]

def palindromes_of_length_at_least_n(s, n=150):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i:j + 1]) and len(s[i:j + 1]) >= n:
                palindromes.add(s[i:j + 1])
    return palindromes