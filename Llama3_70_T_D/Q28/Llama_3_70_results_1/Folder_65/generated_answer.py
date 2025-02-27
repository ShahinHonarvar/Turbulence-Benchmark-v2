def return_nth_smallest_ascii(s):
    s = ''.join((c for i, c in enumerate(s) if 32 <= i <= 67))
    return sorted(s)[11]