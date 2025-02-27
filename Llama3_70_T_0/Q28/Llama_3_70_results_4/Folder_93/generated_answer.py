def return_nth_smallest_ascii(s):
    return sorted([c for i, c in enumerate(s) if 42 <= i <= 59])[16]