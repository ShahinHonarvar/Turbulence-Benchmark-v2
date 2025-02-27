def palindrome_of_length_n(s):
    """
            s: the input string
            """
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 275):
        if s[i:i + 276] == s[i:i + 276][::-1]:
            palindromes.add(s[i:i + 276])
    return palindromes