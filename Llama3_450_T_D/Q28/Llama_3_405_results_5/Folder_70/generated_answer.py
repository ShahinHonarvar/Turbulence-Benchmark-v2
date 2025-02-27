def return_nth_smallest_ascii(s):
    slice_s = s[28:55]
    ascii_sorted = sorted(slice_s, key=lambda x: ord(x))
    return ascii_sorted[13]