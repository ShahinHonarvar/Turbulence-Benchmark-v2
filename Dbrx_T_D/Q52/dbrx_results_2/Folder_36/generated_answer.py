def palindrome_of_length_n(s):
    s = s.lower()
    n = 338
    palindromes = set()
    for i in range(len(s) - n + 1):
        if all((s[i + j] == s[i + n - 1 - j] for j in range((n - 1) // 2))):
            palindromes.add(s[i:i + n])
    return palindromes