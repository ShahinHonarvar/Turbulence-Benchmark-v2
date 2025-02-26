def return_nth_smallest_ascii(s):
    if len(s) < 6:
        return None
    substring = s[:6]
    sorted_chars = sorted(substring)
    return sorted_chars[5]