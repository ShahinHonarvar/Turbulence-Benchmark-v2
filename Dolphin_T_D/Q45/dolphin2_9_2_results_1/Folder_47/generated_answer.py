def palindromes_between_indices(s):
    sub = ''.join((c.lower() for c in s[2:8] if c.isalpha()))
    return {s[3:8] + s[8:5:-1] for s in sub ** 5 if ''.join(sorted(s)) not in {''.join(sorted(p)) for p in sub ** 5 if len(p) < 5}}