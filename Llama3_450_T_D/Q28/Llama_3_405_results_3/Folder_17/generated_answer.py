def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 4 <= i <= 33])
    return sorted(chars, key=lambda c: ord(c))[3]