def palindrome_of_length_n(s):
    n = 20
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - n + 1):
        palindrome = s[i:i + n]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes