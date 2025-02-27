def return_nth_smallest_ascii(s):
    v = sorted([c for i, c in enumerate(s) if 10 <= i <= 90])
    return v[19]