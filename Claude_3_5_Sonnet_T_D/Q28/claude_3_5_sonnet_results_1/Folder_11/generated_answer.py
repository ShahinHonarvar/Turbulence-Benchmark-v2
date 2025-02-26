def return_nth_smallest_ascii(s):
    subset = s[9:60]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 6:
        return sorted_chars[5]
    return None