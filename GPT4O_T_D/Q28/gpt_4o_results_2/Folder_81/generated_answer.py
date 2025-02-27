def return_nth_smallest_ascii(s):
    return sorted(s[:14])[13] if len(s) >= 14 else None