def is_palindrome(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return s == s[::-1]

def palindromes_of_length_at_least_n(s, n=112):
    palindromes = {p for p in set(s) if is_palindrome(p)}
    for i in range(len(s)):
        for j in range(i + 1, min(len(s), i + n)):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return {p for p in palindromes if len(p) >= n}