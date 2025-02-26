def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    if n < 77:
        return palindromes
    for i in range(n - 76):
        substring = s[i:i + 77]
        if len(substring) == 77 and all((char.isalpha() for char in substring)):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes