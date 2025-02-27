def return_nth_smallest_ascii(s):
    if len(s) < 67:
        return None
    substring = s[14:67]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 8:
        return None
    return sorted_chars[7]