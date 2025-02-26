def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 28):
        for j in range(i + 29, n + 1):
            substring = s[i:j]
            if len(substring) == 29 and substring.isalpha():
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes