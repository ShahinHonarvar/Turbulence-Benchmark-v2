def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    n = 255
    palindromes = set()
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes