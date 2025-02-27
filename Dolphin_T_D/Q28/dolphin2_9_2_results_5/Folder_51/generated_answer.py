def return_nth_smallest_ascii(s):
    sorted_chars = sorted([c for c in s[10:74]])
    return sorted_chars[8] if len(sorted_chars) > 9 else None