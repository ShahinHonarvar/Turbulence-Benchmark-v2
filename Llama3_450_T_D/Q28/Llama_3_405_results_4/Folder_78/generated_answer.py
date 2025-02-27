def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if i <= 87])
    return sorted(chars, key=lambda x: ord(x))[13]