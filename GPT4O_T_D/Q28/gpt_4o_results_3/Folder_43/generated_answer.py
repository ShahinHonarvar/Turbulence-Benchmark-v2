def return_nth_smallest_ascii(s):
    if len(s) < 36:
        return None
    sliced_chars = s[14:36]
    sorted_chars = sorted(sliced_chars)
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]