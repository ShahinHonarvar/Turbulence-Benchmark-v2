def return_nth_smallest_ascii(s):
    if len(s) < 69:
        return None
    return sorted(s[34:69])[5]