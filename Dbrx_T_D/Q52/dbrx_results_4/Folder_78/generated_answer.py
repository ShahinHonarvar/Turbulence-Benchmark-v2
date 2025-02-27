from collections import defaultdict
import re

def palindrome_of_length_n(string, n=48):
    palindromes = set()
    string = re.sub('[^a-zA-Z]', '', string.lower())
    if len(string) < n:
        return palindromes
    dp = [[False] * len(string) for _ in range(len(string))]
    for i in range(len(string)):
        dp[i][i] = True
    for k in range(1, n):
        for i in range(len(string) - k):
            j = i + k
            if k == 1:
                dp[i][j] = string[i] == string[j]
            else:
                dp[i][j] = string[i] == string[j] and dp[i + 1][j - 1]
            if dp[i][j]:
                palindromes.add(string[i:j + 1])
    return palindromes