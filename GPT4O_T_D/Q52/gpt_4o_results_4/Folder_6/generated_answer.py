def palindrome_of_length_n(s):
    s = ''.join([c.lower() for c in s if c.isalpha()])
    palindromes = set()
    n = 474
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes