def palindromes_between_indices(s):
    letters_in_range = [c.lower() for c in s[:3]]
    return set((''.join(p) for p in product(letters_in_range, repeat=3) if p == p[::-1] and p != p[0] * 3))