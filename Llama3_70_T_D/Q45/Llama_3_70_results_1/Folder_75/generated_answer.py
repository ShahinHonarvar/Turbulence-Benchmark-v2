def palindromes_between_indices(s):
    s = s[2:5].lower()
    letters = [c for c in s if c.isalpha()]
    pals = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        pal = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[l] + letters[k] + letters[j] + letters[i]
                        pals.add(pal)
    return pals