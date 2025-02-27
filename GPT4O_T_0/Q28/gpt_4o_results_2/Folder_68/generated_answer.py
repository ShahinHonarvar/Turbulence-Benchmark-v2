def return_nth_smallest_ascii(s):
    if len(s) < 11:
        return None
    return sorted(s[:11])[10]