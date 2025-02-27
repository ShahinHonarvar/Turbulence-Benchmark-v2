def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 9 <= i <= 59])
    return chars[5]