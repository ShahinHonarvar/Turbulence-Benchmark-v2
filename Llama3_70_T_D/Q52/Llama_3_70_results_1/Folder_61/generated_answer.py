def palindrome_of_length_n(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 73):
        substring = s[i:i + 74]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes