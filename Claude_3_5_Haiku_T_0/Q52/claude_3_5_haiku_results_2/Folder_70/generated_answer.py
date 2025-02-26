def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 400):
        for j in range(i + 401, n + 1):
            substring = s[i:j]
            if len(substring) == 401 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes