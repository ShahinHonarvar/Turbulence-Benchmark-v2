def return_nth_smallest_ascii(s):
    return sorted(s[:46])[9] if len(s) >= 10 else None