def return_nth_smallest_ascii(s):
    subset = s[:16]
    sorted_chars = sorted(subset)
    return sorted_chars[15] if len(sorted_chars) >= 16 else None