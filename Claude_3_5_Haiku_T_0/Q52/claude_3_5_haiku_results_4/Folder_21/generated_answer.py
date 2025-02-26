def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 406):
        for j in range(i + 407, n + 1):
            substring = s[i:j]
            if len(substring) == 407 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes