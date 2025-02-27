def return_nth_smallest_ascii(s):
    slice_ = s[10:83]
    unique_chars = sorted(set(slice_))
    return unique_chars[17]