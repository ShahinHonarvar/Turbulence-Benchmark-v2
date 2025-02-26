def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 62):
        substring = s[i:i + 63]
        if len(substring) == 63 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes