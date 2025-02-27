def return_nth_smallest_ascii(s):
    slice_s = s[5:83]
    unique_chars = sorted(set(slice_s))
    return unique_chars[15]