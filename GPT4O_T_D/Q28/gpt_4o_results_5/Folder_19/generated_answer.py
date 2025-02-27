def return_nth_smallest_ascii(s):
    if len(s) < 19:
        return None
    return sorted(s[:19])[12]