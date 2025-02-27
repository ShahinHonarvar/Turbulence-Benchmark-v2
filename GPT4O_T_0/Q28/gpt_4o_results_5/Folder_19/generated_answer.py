def return_nth_smallest_ascii(s):
    return sorted(s[:19])[12] if len(s) >= 13 else None