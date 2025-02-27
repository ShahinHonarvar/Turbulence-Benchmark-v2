def return_nth_smallest_ascii(s):
    return sorted(s[:13])[12] if len(s) >= 13 else None