def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 22 <= i <= 74])
    return chars[11]