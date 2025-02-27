import re
from collections import defaultdict

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = 366
    if len(s) < n:
        return palindromes
    dp = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i + 1 == n:
                    palindromes.add(s[i:j + 1])
    return palindromes

def find_palindromes(s):
    s = re.sub('[^a-zA-Z]', '', s)
    return palindrome_of_length_n(s)