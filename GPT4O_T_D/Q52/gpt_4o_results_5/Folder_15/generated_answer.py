def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 3):
        substring = s[i:i + 4]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes