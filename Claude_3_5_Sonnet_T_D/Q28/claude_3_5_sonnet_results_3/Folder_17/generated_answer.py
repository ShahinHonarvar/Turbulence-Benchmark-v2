def return_nth_smallest_ascii(s):
    subset = s[4:34]
    sorted_chars = sorted(subset)
    return sorted_chars[3] if len(sorted_chars) >= 4 else None