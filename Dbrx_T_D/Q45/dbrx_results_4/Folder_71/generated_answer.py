def palindromes_between_indices(s):
    letters = {c.lower() for c in s[1:4]}
    palindromes = {w for w in letters if len(w) >= 4}
    for i in range(1, 4):
        for j in range(i, 4):
            sub = s[i:j + 1]
            sub = {c.lower() for c in sub}
            for c in sub:
                if c not in letters:
                    sub.remove(c)
            if len(sub) >= 4:
                palindromes.add(''.join(sorted(sub)))
    return palindromes