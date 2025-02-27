def palindromes_between_indices(txt):
    letters = ''.join(sorted([c.lower() for c in txt[0:6] if c.isalpha()]))
    return {l[i:i + 3] for i in range(len(l) - 2) for l in [letters] if l[i:i + 3] == l[i:i + 3][::-1]}