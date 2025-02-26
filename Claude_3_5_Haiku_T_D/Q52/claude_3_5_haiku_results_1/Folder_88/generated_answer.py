def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 12):
        for end in range(start + 13, n + 1):
            substring = s[start:end]
            if len(substring) == 13 and substring == substring[::-1]:
                if all((char.isalpha() for char in substring)):
                    palindromes.add(substring)
    return palindromes