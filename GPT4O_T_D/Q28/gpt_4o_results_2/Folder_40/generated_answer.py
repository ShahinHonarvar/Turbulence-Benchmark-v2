def return_nth_smallest_ascii(s):
    if len(s) < 5:
        return None
    return sorted(s[:5])[4]