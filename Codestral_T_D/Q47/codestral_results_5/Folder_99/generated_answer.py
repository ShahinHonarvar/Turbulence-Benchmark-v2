def palindromes_of_specific_lengths(s):
    s = s[127:289]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 119, min(i + 142, len(s))):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes