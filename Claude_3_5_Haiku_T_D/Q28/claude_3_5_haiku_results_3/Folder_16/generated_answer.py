def return_nth_smallest_ascii(s):
    subset = s[18:46]
    sorted_chars = sorted(set(subset))
    return sorted_chars[6] if len(sorted_chars) >= 7 else None