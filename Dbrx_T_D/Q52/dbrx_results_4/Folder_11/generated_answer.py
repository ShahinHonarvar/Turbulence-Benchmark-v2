def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = 77
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i, min(i + n + 1, len(s) + 1)) if s[i:j] == s[i:j][::-1]}
    return palindromes