def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 40):
        substring = s[i:i + 41]
        if all((c.isalpha() for c in substring)):
            if substring[::-1] == substring:
                palindromes.add(substring)
    return palindromes