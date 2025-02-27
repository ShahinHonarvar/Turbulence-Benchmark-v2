def palindrome_of_length_n(s):
    s = s.lower()
    n = 93
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) == n:
                palindromes.add(substring)
    return palindromes