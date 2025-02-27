def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 51 <= i <= 60])
    return chars[4]