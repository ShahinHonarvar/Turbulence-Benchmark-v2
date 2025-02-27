def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = 35
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s), n):
            if s[i:i + n] == s[i:i + n][::-1]:
                palindromes.add(s[i:j])
    return palindromes