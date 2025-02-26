def return_nth_smallest_ascii(s):
    subset = s[:13]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 13:
        return sorted_chars[12]
    else:
        return sorted_chars[-1]