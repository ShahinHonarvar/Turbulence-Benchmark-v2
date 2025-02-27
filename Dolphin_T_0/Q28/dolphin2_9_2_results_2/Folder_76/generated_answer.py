def return_nth_smallest_ascii(s):
    return sorted([ch for i, ch in enumerate(s) if 18 <= i <= 66])[18]