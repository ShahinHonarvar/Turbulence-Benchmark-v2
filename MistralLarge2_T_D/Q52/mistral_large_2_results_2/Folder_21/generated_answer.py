def palindrome_of_length_n(s):
    n = 407
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes