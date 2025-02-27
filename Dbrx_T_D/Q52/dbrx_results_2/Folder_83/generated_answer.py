from collections import defaultdict

def is_palindrome(s):
    return all((s[i] == s[-i - 1] for i in range(len(s) // 2)))

def to_palindrome(s):
    return ''.join((c for c in s if c.isalpha())).lower()

def palindrome_of_length_n(string, n):
    if n % 2 == 0:
        center = n // 2
    else:
        center = (n - 1) // 2
    string = to_palindrome(string)
    chars = defaultdict(list)
    for i in range(len(string)):
        for j in range(min(i, center, len(string) - i - 1)):
            substring = string[i - j - 1:i] + string[i] + string[i + 1:i + j + 2]
            if is_palindrome(substring):
                chars[substring].append((i, y))
    palindromes = set()
    for palindrome in chars:
        palindromes.add(palindrome)
    return palindromes