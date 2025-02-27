def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if i <= 5])
    return chars[5]