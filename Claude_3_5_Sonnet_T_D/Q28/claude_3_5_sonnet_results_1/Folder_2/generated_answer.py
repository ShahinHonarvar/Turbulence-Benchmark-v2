def return_nth_smallest_ascii(s):
    subset = s[48:77]
    sorted_chars = sorted(subset)
    return sorted_chars[4] if len(sorted_chars) >= 5 else None