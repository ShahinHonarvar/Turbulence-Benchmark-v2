def return_nth_smallest_ascii(s):
    if len(s) < 88:
        return None
    return sorted(s[:88])[13]