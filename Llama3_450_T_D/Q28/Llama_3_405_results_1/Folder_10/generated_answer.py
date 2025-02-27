def return_nth_smallest_ascii(s):
    substr = s[38:83]
    unique_chars = sorted(set(substr))
    return unique_chars[19]