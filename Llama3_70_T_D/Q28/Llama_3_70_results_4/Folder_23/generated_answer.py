def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 29 <= i <= 47])
    return chars[6]