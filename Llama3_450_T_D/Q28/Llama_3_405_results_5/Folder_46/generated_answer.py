def return_nth_smallest_ascii(s):
    slice_of_string = s[34:86]
    ascii_chars = sorted(set(slice_of_string))
    return ascii_chars[19]