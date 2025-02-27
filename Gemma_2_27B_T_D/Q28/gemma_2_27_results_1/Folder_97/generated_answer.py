def return_nth_smallest_ascii(s):
    slice_ = s[15:22]
    return sorted(slice_, key=ord)[5]