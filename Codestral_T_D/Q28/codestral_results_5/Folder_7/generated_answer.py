def return_nth_smallest_ascii(s):
    substr = s[12:56]
    sorted_chars = sorted(substr)
    return sorted_chars[16]