def return_nth_smallest_ascii(s):
    if len(s) < 83:
        return None
    sliced_chars = s[5:83]
    sorted_chars = sorted(sliced_chars)
    if len(sorted_chars) < 16:
        return None
    return sorted_chars[15]