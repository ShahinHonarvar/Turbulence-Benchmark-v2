def return_nth_smallest_ascii(s):
    if len(s) < 68:
        return None
    substring = s[28:68]
    sorted_chars = sorted(substring, key=lambda c: ord(c))
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]