def return_nth_smallest_ascii(s):
    s_slice = s[5:48]
    unique_chars = sorted(set(s_slice))
    return unique_chars[12]