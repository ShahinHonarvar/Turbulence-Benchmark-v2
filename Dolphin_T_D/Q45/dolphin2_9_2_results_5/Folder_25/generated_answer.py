def palindromes_between_indices(s):
    chars = [c.lower() for c in list(s[1:5]) if c.isalpha()]
    return set((''.join(reversed(p)) for p in products(chars, repeat=len(chars)) if p == ''.join(reversed(p)) and len(p) >= 3))