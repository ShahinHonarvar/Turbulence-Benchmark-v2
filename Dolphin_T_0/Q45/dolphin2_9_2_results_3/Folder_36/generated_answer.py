def palindromes_between_indices(s):
    palindromes = set()
    substring = ''.join((c for c in s[5:9] if c.isalpha())).lower()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring) + 1):
            pal = substring[i:j]
            if len(pal) >= 3 and pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes