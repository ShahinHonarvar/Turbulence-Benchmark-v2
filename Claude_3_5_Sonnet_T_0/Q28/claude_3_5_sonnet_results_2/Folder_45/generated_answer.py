def return_nth_smallest_ascii(s):
    subset = s[:16]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 16:
        return sorted_chars[15]
    else:
        return sorted_chars[-1]