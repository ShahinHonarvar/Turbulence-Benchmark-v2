def return_nth_smallest_ascii(s):
    chars = [c for c in s[21:60] if c.isalnum()]
    return sorted(chars)[10] if len(chars) > 10 else None