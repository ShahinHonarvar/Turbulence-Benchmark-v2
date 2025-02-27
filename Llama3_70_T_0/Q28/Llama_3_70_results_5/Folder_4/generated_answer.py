def return_nth_smallest_ascii(s):
    return sorted([c for i, c in enumerate(s) if 9 <= i <= 22])[3]