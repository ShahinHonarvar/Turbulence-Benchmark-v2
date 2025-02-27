def return_nth_smallest_ascii(s):
    return sorted([c for i, c in enumerate(s) if 10 <= i <= 82])[17]