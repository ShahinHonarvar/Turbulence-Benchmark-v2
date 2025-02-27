def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 41):
        for j in range(i, len(s) - 40):
            if s[i:j + 1] == s[i:j + 1][::-1] and len(s[i:j + 1]) >= 42:
                palindromes.add(s[i:j + 1])
    return palindromes