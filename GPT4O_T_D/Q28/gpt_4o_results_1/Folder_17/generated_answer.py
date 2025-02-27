def return_nth_smallest_ascii(s):
    if len(s) < 34:
        chars_in_range = s[4:]
    else:
        chars_in_range = s[4:34]
    sorted_chars = sorted(chars_in_range, key=lambda x: ord(x))
    return sorted_chars[3] if len(sorted_chars) >= 4 else None