def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 337):
        for end in range(start + 338, n + 1):
            substring = s[start:end]
            if len(substring) == 338 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes