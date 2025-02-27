def palindromes_between_indices(s):
    letters = set()
    for i in range(0, 8):
        if s[i].isalpha():
            letters.add(s[i].lower())
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(0, 5):
        for j in range(i + 2, 8):
            if len(letters) > 4 and i + j - 1 < 7 and (i in [0, 1]) and (j in [5, 7]):
                pal = s[i] + s[j]
                for k in range(i + 1, j):
                    pal += s[k]
                if pal == pal[::-1] and len(pal) >= 6:
                    palindromes.add(pal)
    return palindromes