def return_nth_smallest_ascii(s):
    if len(s) < 82:
        return None
    sorted_chars = sorted(s[34:82], key=lambda x: ord(x))
    if len(sorted_chars) < 12:
        return None
    return sorted_chars[11]