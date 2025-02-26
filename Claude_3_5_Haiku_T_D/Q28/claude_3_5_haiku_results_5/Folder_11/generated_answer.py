def return_nth_smallest_ascii(s):
    subset = s[9:60]
    sorted_chars = sorted(set(subset))
    return sorted_chars[5] if len(sorted_chars) >= 6 else None