def return_nth_smallest_ascii(s):
    if len(s) < 68:
        return None
    segment = s[28:68]
    sorted_chars = sorted(segment)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]