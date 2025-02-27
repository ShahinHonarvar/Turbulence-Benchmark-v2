def return_nth_smallest_ascii(s):
    if len(s) < 35:
        return None
    substring = s[17:35]
    sorted_chars = sorted(substring)
    return sorted_chars[17]