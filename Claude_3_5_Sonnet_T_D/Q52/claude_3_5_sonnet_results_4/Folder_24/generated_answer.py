def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes