def return_nth_smallest_ascii(s):
    subset = s[42:60]
    sorted_chars = sorted(subset)
    return sorted_chars[16] if len(sorted_chars) >= 17 else None