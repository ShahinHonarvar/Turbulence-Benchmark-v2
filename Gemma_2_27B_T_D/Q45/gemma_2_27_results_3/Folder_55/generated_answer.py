def palindromes_between_indices(text):
    letters = ''.join([c for c in text[:3] if c.isalpha()]).lower()
    return {p for p in set((''.join(p) for p in permutations(letters))) if len(p) >= 3 and p == p[::-1]}