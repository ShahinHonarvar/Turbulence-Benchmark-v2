def return_nth_smallest_ascii(s):
    subset = s[12:88]
    sorted_chars = sorted(set(subset))
    if len(sorted_chars) >= 17:
        return sorted_chars[16]
    return None