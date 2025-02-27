def return_nth_smallest_ascii(s):
    return sorted(s[:17])[16] if len(s) >= 17 else None