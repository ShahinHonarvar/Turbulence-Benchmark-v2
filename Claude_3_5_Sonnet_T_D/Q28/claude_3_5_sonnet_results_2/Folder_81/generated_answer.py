def return_nth_smallest_ascii(s):
    subset = s[:14]
    sorted_chars = sorted(subset)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None