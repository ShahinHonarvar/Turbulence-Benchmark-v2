def return_nth_smallest_ascii(s):
    subset = s[14:55]
    sorted_chars = sorted(subset)
    return sorted_chars[10] if len(sorted_chars) > 10 else None