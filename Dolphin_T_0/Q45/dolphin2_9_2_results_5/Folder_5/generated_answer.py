def palindromes_between_indices(s):
    palindromes = set()
    substring = s[4:9].lower()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            pal = substring[i:j]
            if pal == pal[::-1] and len(pal) >= 4:
                palindromes.add(pal)
    return palindromes