from collections import defaultdict

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 35 + 1):
        substring = s[i:i + 35]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])