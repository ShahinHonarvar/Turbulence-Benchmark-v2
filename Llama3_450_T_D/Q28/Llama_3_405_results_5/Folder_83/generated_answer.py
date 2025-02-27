def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 30 <= i <= 70])
    return chars[14]