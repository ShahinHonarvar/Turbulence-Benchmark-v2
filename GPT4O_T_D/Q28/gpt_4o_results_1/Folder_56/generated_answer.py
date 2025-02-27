def return_nth_smallest_ascii(s):
    return sorted(s[:5])[3] if len(s) >= 4 else None