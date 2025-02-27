def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 9, len(s)):
            if len(set([s[i:j + 1][k] for k in range(len(s[i:j + 1]) // 2) if s[i:j + 1][k] != s[i:j + 1][-(k + 1)]])) == 0:
                palindromes.add(s[i:j + 1])
    return palindromes