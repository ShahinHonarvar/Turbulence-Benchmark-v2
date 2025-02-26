def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 6):
        substring = s[i:i + 7]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes