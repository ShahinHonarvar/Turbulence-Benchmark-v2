def return_nth_smallest_ascii(s):
    if len(s) < 36:
        return None
    substring = s[13:36]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 18:
        return None
    return sorted_chars[17]