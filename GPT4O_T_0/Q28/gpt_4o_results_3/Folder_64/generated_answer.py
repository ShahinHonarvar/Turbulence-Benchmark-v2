def return_nth_smallest_ascii(s):
    return sorted(s[:7])[6] if len(s) >= 7 else None