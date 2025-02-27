def return_nth_smallest_ascii(s):
    substring = s[34:86]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 20:
        return sorted_chars[19]
    return None