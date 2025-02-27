def return_nth_smallest_ascii(s):
    substring = s[51:90]
    if len(substring) < 14:
        raise ValueError('The string does not contain enough characters within the specified range.')
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None