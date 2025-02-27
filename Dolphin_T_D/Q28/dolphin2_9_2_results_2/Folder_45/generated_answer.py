def return_nth_smallest_ascii(s):
    return sorted(s[:16])[15] if len(s) > 15 else sorted(s)[len(s) - 1]