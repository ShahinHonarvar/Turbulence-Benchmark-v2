from collections import defaultdict

def palindromes_of_length_n(s, n):
    if n % 2 == 1:
        return set()
    chars = defaultdict(lambda: set())
    for i in range(len(s)):
        chars[s[i]].add(i)
    result = set()
    for i in range(len(s) - n + 1):
        for j in chars[s[i]]:
            if j <= i or j >= i + n - 1:
                continue
            for k in range(j - 1, i - 1, -2):
                if k >= len(s) or s[k] != s[i + j - k]:
                    break
            else:
                palindrome = s[i:i + n]
                if palindrome.isalpha():
                    result.add(palindrome.lower())
    return result