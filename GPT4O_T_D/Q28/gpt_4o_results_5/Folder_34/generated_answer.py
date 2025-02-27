def return_nth_smallest_ascii(s):
    return sorted(s[:19])[18] if len(s) >= 19 else None