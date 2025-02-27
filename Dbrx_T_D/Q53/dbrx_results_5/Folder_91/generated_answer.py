def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 6):
        for j in range(i, len(s) - i):
            if s[i:j + 1] == s[i:j + 1][::-1] and len(s[i:j + 1]) >= 7:
                palindromes.add(s[i:j + 1])
    return palindromes