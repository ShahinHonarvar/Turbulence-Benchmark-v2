def return_nth_smallest_ascii(s):
    slice_s = s[50:77]
    sorted_slice = sorted(slice_s, key=lambda c: ord(c))
    return sorted_slice[10]