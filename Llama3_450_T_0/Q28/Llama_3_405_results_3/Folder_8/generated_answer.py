def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 60 <= i <= 88])
    return chars[6]