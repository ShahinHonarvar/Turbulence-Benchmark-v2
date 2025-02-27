from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = {chr(i) for i in range(ord('a'), ord('z') + 1)} | {chr(i) for i in range(ord('A'), ord('Z') + 1)}
    s = s[4:9].lower()
    s = ''.join((c for c in s if c in eng_letters))
    if len(s) < 2:
        return set()
    dp = [[0] * len(s) for _ in range(len(s))]
    palindrome_set = set()
    for i in range(len(s)):
        dp[i][i] = True
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            palindrome_set.add(s[i:i + 2])
    for k in range(3, len(s) + 1):
        for i in range(len(s) - k + 1):
            j = i + k - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                palindrome_set.add(s[i:j + 1])
    return palindrome_set