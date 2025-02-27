def palindrome_of_length_at_least_n(s):
    n = 53
    palindromes = set()
    for i in range(len(s) - n + 1):
        if all((c.lower() == s[i + n - c - 1].lower() for c in range(1, n // 2 + 1))):
            palindromes.add(s[i:i + n])
    return palindromes