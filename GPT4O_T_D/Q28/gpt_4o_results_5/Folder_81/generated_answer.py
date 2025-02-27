def return_nth_smallest_ascii(s):
    if len(s) < 14:
        return None
    return sorted(s[:14])[13]