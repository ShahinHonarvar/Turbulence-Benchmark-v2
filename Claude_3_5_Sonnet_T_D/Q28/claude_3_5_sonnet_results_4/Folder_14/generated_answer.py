def return_nth_smallest_ascii(s):
    substring = s[46:83]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 16:
        return sorted_chars[15]
    return None