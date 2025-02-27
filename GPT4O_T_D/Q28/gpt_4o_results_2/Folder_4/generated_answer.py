def return_nth_smallest_ascii(s):
    if len(s) <= 22:
        return None
    substring = s[9:23]
    if len(substring) < 4:
        return None
    sorted_chars = sorted(substring)
    return sorted_chars[3]