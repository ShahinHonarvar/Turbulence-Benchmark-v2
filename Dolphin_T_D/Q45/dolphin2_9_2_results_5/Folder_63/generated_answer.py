def palindromes_between_indices(s):
    s = s[:4].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            pal = s[i:j]
            if pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes