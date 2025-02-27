def return_nth_smallest_ascii(s):
    if len(s) < 7:
        return None
    return sorted(s[:7])[6]