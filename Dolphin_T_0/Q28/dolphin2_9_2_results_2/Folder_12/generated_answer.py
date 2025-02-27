def return_nth_smallest_ascii(s):
    ordered = sorted([c for i, c in enumerate(s) if 3 <= i <= 26])
    return ordered[4]