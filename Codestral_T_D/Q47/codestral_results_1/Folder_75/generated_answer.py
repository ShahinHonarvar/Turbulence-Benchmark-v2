def palindromes_of_specific_lengths(s):
    s = s[31:75]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 23, i + 40):
            if j <= len(s) and s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes