def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    length = 318
    if length > len(s):
        return set()
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes