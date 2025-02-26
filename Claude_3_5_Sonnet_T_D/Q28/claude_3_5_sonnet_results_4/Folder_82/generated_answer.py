def return_nth_smallest_ascii(s):
    subset = s[:15]
    sorted_chars = sorted(subset)
    return sorted_chars[14] if len(sorted_chars) >= 15 else None