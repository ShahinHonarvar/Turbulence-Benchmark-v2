def palindromes_between_indices(s):
    sub = s[3:8].lower()
    length = len(sub)
    n = length // 2
    palindromes = set()
    for i in range(1 << n):
        pal = ''
        for j in range(n):
            if i & 1 << j:
                pal += sub[j]
            else:
                pal += sub[j + n]
        if len(pal) >= 6:
            if pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes