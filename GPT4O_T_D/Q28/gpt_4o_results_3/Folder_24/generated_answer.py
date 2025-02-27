def return_nth_smallest_ascii(s):
    if len(s) < 82:
        return None
    substring = s[34:82]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 12:
        return None
    return sorted_chars[11]