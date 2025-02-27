def return_nth_smallest_ascii(s):
    substring = s[10:91]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 20:
        return None
    return sorted_chars[19]