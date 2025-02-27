def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 63 <= i <= 76]
    return sorted(chars, key=lambda x: ord(x))[13]