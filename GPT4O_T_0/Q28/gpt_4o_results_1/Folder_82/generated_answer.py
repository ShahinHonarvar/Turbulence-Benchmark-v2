def return_nth_smallest_ascii(s):
    if len(s) < 15:
        return None
    return sorted(s[:15])[14]