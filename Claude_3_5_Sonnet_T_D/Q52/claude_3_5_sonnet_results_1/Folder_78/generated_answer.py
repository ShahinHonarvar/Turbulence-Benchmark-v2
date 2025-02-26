def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    palindromes = set()
    for i in range(n - 47):
        substring = s[i:i + 48]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes