def return_nth_smallest_ascii(s):
    if len(s) < 17:
        return None
    return sorted(s[:17])[16]