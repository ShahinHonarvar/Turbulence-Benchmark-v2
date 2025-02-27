def palindrome_of_length_n(s):
    n = 72
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if len(s) < n:
        return set()
    palindromes = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1] and s[i:i + n].isalpha():
            palindromes.add(s[i:i + n])
    return palindromes