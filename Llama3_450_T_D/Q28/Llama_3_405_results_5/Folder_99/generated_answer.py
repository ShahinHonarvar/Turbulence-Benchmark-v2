def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 17 <= i <= 65])
    return sorted(chars, key=lambda x: ord(x))[7]