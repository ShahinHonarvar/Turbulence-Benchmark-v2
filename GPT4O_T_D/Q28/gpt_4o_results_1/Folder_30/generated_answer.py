def return_nth_smallest_ascii(s):
    if len(s) < 77:
        return None
    substring = s[50:77]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]