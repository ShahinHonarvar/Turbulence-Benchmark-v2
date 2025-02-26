def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 42):
        substring = s[i:i + 43]
        if len(substring) == 43 and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes