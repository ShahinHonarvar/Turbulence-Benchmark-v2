from collections import defaultdict

def palindrome_of_length_n(s):
    s = s.lower()
    n = 21
    if len(s) < n:
        return set()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes

def is_palindrome(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    odd_count = 0
    for count in d.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count <= 1