def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    if n >= 64:
        for i in range(n - 63):
            substring = s[i:i + 64]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes