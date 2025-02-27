def return_nth_smallest_ascii(s):
    if len(s) < 46:
        return None
    return sorted(s[:46])[9]