def return_nth_smallest_ascii(s):
    subset = s[:10]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 10:
        return sorted_chars[9]
    else:
        return sorted_chars[-1]