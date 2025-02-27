def return_nth_smallest_ascii(s):
    substr = s[44:70]
    ascii_chars = sorted(list(substr))
    return ascii_chars[14]