def return_nth_smallest_ascii(s):
    if len(s) < 16:
        return sorted(s)[len(s) - 1]
    return sorted(s[:16])[15]