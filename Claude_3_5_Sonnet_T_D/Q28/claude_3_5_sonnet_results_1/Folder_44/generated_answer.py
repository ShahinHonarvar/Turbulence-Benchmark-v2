def return_nth_smallest_ascii(s):
    substring = s[20:31]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 8:
        return sorted_chars[7]
    else:
        return None