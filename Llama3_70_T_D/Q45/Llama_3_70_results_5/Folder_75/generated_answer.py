def palindromes_between_indices(s):
    s = s[2:5].lower()
    pals = set()
    for c in 'abcdefghijklmnopqrstuvwxyz':
        for d in 'abcdefghijklmnopqrstuvwxyz':
            pals.add(c + d + c)
            pals.add(d + c + d)
    return set((pal for pal in pals if set(pal).issubset(set(s)) and len(set(pal)) > 1))