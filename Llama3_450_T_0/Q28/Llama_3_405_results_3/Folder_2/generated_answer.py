def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 48 <= i <= 76], key=lambda x: ord(x))
    return chars[4]