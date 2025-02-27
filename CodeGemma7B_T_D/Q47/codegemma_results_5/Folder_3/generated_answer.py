def palindromes_of_specific_lengths(string):
    dp = [[False] * 70 for _ in range(2000)]
    for i in range(len(string) - 1, -1, -1):
        for j in range(i + 1, len(string)):
            if string[i].lower() == string[j].lower() and dp[i + 1][j - 1]:
                dp[i][j] = True
    palindromes = set()
    for i in range(27, 96):
        for j in range(i + 49, i + 52):
            if dp[i][j]:
                palindromes.add(string[i:j + 1].lower())
    return palindromes