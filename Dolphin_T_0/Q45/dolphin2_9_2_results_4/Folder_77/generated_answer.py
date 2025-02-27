def palindromes_between_indices(string):
    letters = set()
    for c in string[4:7]:
        if c.isalpha():
            letters.add(c.lower())
    res = set()
    if len(letters) < 2:
        return res
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    p = a + b + c + d
                    if p == p[::-1]:
                        res.add(p)
    return res