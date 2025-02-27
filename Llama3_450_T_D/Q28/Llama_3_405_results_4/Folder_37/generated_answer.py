def return_nth_smallest_ascii(s):
    slice = s[28:68]
    sorted_slice = sorted(slice, key=lambda c: ord(c))
    return sorted_slice[14]