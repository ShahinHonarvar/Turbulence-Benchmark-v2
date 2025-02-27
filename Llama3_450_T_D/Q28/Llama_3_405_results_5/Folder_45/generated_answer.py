def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if i <= 15])
    return min(chars, key=lambda c: abs(ord(c) - sorted([ord(c) for c in chars])[15]))