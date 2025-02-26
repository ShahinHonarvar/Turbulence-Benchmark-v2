def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if len(substring) >= 144 and substring == substring[::-1]:
                if all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes