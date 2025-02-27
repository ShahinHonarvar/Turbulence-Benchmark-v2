def return_nth_smallest_ascii(s):
    if len(s) < 86:
        return None
    substring = s[34:86]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 20:
        return None
    return sorted_chars[19]