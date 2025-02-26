def return_nth_smallest_ascii(s):
    subset = s[10:74]
    sorted_chars = sorted(subset)
    return sorted_chars[8] if len(sorted_chars) >= 9 else None