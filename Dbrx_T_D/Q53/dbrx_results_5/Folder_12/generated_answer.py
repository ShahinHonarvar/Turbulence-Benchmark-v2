from collections import defaultdict

def is_palindrome(s, start, end):
    while start < end:
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True

def palindrome_of_length_at_least_n(s):
    n = 51
    palindromes = set()
    if len(s) < n:
        return palindromes
    s = [char.lower() for char in s]
    for i in range(len(s) - n + 1):
        for j in range(i, len(s) - n + 2):
            if is_palindrome(s, i, j - 1):
                palindromes.add(''.join(s[i:j]))
    return palindromes