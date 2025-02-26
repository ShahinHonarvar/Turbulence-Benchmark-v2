def return_nth_smallest_ascii(s):
    subset = s[34:82]
    sorted_chars = sorted(subset)
    return sorted_chars[11] if len(sorted_chars) >= 12 else None