def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

def find_palindromes(s):
    return {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if is_palindrome(s[i:j])}

def palindrome_of_length_at_least_n(s, n=60):
    return {p for p in find_palindromes(s) if len(p) >= n}