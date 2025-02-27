def return_nth_smallest_ascii(s):
    return sorted(s[:5])[4] if len(s) >= 5 else None