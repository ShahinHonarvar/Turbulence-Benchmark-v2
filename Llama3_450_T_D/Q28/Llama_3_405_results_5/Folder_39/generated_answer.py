def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 1 <= i <= 66])
    return chars[7]