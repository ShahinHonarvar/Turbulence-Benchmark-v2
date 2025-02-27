def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 52 <= i <= 79])
    return chars[6]