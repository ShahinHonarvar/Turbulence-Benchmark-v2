def return_nth_smallest_ascii(s):
    slice_s = s[0:12]
    return sorted(slice_s, key=lambda x: ord(x))[11]