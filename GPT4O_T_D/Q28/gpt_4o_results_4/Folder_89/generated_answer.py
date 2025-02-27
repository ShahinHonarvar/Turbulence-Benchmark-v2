def return_nth_smallest_ascii(s):
    if len(s) < 72:
        return None
    substring = s[24:72]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 8:
        return None
    return sorted_chars[7]