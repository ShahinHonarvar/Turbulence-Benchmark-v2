def return_nth_smallest_ascii(s):
    return sorted([c for i, c in enumerate(s) if 46 <= i <= 72])[14]