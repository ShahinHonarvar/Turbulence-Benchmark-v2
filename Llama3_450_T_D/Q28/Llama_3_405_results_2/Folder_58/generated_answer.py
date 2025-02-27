def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 8 <= i <= 26])
    return sorted(chars, key=lambda x: ord(x))[5]