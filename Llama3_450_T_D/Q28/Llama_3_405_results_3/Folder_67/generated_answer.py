def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 60 <= i <= 83])
    return sorted(chars, key=lambda x: ord(x))[13]