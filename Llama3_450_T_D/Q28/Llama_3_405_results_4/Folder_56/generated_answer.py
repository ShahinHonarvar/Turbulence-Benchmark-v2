def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if i <= 4])
    return sorted(chars, key=lambda x: x)[3]