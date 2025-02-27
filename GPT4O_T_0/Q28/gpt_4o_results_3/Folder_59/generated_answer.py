def return_nth_smallest_ascii(s):
    return sorted(s[:12])[11] if len(s) >= 12 else None