def return_nth_smallest_ascii(s):
    return sorted([c for i, c in enumerate(s) if 5 <= i <= 89])[12]