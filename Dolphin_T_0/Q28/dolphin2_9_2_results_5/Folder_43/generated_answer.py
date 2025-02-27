def return_nth_smallest_ascii(s):
    slice_str = s[14:36]
    sorted_str = sorted(slice_str, key=lambda c: ord(c))
    return sorted_str[10]