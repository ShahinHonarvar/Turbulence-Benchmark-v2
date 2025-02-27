def return_nth_smallest_ascii(s):
    return sorted(s[:8])[7] if len(s) >= 8 else None