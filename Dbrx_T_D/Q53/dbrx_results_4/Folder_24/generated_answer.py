def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 1, min(len(s), i + 53)) if s[i:j] == s[i:j][::-1]}
    return palindromes