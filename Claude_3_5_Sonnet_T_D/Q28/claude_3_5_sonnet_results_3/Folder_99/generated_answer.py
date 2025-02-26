def return_nth_smallest_ascii(s):
    subset = s[17:66]
    sorted_chars = sorted(subset)
    return sorted_chars[7] if len(sorted_chars) >= 8 else None