def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 32 <= i <= 67])
    return sorted(chars, key=lambda x: ord(x))[11]