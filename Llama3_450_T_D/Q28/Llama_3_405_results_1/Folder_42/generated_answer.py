def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 12 <= i <= 72])
    return chars[12]