def return_nth_smallest_ascii(s):
    if len(s) < 70:
        return None
    return sorted(s[:70])[9]