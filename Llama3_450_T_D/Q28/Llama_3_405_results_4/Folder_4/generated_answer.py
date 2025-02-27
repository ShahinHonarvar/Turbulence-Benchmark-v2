def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 9 <= i <= 22])
    return chars[3]