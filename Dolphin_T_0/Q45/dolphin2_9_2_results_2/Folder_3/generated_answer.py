def palindromes_between_indices(s):
    letters = set()
    for i in range(7, 10):
        if s[i].isalpha():
            letters.add(s[i].lower())
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                p = a + b + c
                if p == p[::-1] and len(p) >= 3:
                    palindromes.add(p)
    return palindromes