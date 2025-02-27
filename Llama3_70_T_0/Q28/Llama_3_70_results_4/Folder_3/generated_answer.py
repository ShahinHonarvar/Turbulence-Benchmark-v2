def return_nth_smallest_ascii(s):
    return sorted([c for i, c in enumerate(s) if 25 <= i <= 45])[10]