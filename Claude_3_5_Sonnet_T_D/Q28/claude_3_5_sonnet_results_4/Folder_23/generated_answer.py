def return_nth_smallest_ascii(s):
    subset = s[29:48]
    sorted_chars = sorted(subset)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None