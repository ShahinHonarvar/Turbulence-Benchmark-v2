def return_nth_smallest_ascii(s):
    valid_chars = s[12:56]
    sorted_chars = sorted(valid_chars)
    return sorted_chars[16]