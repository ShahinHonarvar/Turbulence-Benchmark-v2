def return_nth_smallest_ascii(s):
    slice_s = s[63:77]
    sorted_slice = sorted(set(slice_s), key=ord)
    return sorted_slice[13]