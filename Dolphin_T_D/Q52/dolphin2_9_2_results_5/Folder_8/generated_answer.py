def palindrome_of_length_n(s):
    s = s.lower()
    n = 49
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if all((c.isalpha() for c in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes