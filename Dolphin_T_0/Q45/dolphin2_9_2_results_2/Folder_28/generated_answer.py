def palindromes_between_indices(s):
    n = len(s)
    palindromes = set()
    if n >= 5:
        for i in range(1, 6):
            for j in range(i + 3, n + 1):
                sub = s[i - 1:j]
                pal = ''.join(reversed(sub))
                if sub == pal:
                    palindromes.add(pal.lower())
    return palindromes