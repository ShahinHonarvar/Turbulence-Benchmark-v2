def return_nth_smallest_ascii(s):
    if len(s) <= 82:
        return None
    substring = s[46:83]
    sorted_chars = sorted(substring)
    return sorted_chars[15]