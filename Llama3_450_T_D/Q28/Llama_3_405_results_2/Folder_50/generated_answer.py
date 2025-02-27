def return_nth_smallest_ascii(s):
    chars = sorted(set([c for i, c in enumerate(s) if 25 <= i <= 88]), key=ord)
    return chars[10]