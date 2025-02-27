def return_nth_smallest_ascii(s):
    return sorted(s[:6])[5] if len(s) >= 6 else None