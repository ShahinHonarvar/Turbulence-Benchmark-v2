def palindromes_of_specific_lengths(s):
    substring = s[2:9]
    palindromes_set = set()
    for i in range(len(substring) - 2):
        for j in range(i + 2, min(i + 4, len(substring)) + 1):
            pal = substring[i:j]
            pal = ''.join((c for c in pal if c.isalpha()))
            if pal == pal[::-1]:
                palindromes_set.add(pal)
    return palindromes_set