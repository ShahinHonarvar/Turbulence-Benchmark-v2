def return_nth_smallest_ascii(s):
    return sorted(s[:11])[10] if len(s) >= 11 else None