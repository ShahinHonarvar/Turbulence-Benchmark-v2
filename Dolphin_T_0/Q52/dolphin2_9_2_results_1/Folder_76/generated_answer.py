def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = 257
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes