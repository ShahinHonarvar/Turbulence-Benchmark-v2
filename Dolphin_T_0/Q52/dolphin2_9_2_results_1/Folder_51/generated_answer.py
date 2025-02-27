def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = 73
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(substring) == n and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes