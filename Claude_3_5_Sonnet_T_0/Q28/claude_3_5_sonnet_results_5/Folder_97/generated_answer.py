def return_nth_smallest_ascii(s):
    subset = s[15:22]
    sorted_chars = sorted(subset)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None