def palindrome_of_length_n(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 471):
        substring = s[i:i + 472]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes