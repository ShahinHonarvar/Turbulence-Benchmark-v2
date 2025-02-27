def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 58 <= i <= 85])
    return sorted(chars, key=lambda x: ord(x))[18]