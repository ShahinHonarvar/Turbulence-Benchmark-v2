def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 47 <= i <= 80])
    return sorted(chars, key=lambda x: ord(x))[3]