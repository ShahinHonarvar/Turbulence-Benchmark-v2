def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 35):
        for j in range(i + 36, len(s), 36):
            if s[i:j] == s[i:j][::-1] and s[j - 36:j] not in (s[i:i + 36], s[i + 36:i + 72]):
                palindromes.add(s[i:j])
    return palindromes