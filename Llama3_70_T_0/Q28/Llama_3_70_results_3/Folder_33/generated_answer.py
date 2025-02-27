def return_nth_smallest_ascii(s):
    return sorted([c for i, c in enumerate(s) if 22 <= i <= 74])[11]