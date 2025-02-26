def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 62):
        for j in range(i + 63, n + 1):
            substring = s[i:j]
            if len(substring) == 63 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes