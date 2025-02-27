def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return {palindrome for i in range(len(s) - 47, len(s) + 1) for j in range(len(s)) for palindrome in [s[j:j + i]] if palindrome == palindrome[::-1] and all((s[k] == s[k + i - j] for k in range(j, j + (i + j) // 2)))}