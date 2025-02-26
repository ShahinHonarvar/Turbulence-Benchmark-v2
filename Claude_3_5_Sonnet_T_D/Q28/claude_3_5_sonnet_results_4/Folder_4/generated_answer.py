def return_nth_smallest_ascii(s):
    subset = s[9:23]
    sorted_chars = sorted(subset)
    return sorted_chars[3] if len(sorted_chars) > 3 else None