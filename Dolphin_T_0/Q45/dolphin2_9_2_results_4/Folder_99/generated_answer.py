def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                p = a + b + c
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes