def palindromes_between_indices(text):
    letters = [c for c in text[:4].lower() if c.isalpha()]
    return set([''.join(p) for p in [list(j) * 2 + [i] + list(j)[::-1] for i, j in [(k, letters[:letters.index(k)]) for k in letters]] if len(''.join(p)) >= 3 and ''.join(p) == ''.join(p)[::-1]])