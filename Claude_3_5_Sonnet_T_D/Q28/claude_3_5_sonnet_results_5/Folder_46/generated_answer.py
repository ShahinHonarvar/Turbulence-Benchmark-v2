def return_nth_smallest_ascii(s):
    subset = s[34:86]
    sorted_chars = sorted(subset)
    return sorted_chars[19] if len(sorted_chars) >= 20 else None