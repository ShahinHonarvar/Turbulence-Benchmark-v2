def return_nth_smallest_ascii(s):
    subset = s[:88]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 14:
        return sorted_chars[13]
    return None