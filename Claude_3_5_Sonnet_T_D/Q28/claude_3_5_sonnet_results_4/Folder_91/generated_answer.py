def return_nth_smallest_ascii(s):
    subset = s[:8]
    sorted_chars = sorted(subset)
    return sorted_chars[7] if len(sorted_chars) >= 8 else None