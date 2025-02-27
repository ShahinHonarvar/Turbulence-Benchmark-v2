def return_nth_smallest_ascii(s):
    return sorted(s[:9])[8] if len(s) >= 9 else None