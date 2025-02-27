def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 6 <= i <= 58])
    return chars[18]