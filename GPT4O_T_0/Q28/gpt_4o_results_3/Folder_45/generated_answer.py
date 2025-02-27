def return_nth_smallest_ascii(s):
    if len(s) < 16:
        return None
    return sorted(s[:16])[15]