def return_nth_smallest_ascii(s):
    subset = s[38:83]
    sorted_chars = sorted(subset)
    return sorted_chars[19] if len(sorted_chars) >= 20 else None