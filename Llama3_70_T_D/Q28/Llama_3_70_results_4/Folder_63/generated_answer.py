def return_nth_smallest_ascii(s):
    return sorted([c for i, c in enumerate(s) if 47 <= i <= 70])[13]