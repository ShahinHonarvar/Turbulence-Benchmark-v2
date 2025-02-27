def return_nth_smallest_ascii(s):
    if len(s) < 8:
        return None
    return sorted(s[:8])[7]