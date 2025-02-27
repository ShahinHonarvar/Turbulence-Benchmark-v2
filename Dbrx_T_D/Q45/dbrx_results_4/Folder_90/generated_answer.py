def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 5:
        return set()
    palindromes = set()
    for i in range(0, min(6, len(s) + 1)):
        for j in range(i, min(6, len(s) + 1)):
            pal = s[i:j][::-1] + s[i:j]
            if len(pal) >= 4 and pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes