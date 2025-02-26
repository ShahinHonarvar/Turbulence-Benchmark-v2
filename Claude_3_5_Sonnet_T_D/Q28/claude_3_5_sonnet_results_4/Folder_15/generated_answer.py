def return_nth_smallest_ascii(s):
    substr = s[:6]
    sorted_chars = sorted(substr)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None