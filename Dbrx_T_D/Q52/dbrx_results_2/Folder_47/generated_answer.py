def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if len(s) < 34:
        return set()
    palindromes = set()
    for i in range(len(s) - 33):
        if s[i:i + 34] == s[i:i + 34][::-1]:
            palindromes.add(s[i:i + 34])
    return palindromes