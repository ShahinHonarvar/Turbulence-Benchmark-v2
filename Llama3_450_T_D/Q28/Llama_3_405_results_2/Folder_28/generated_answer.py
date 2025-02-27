def return_nth_smallest_ascii(s):
    slice_s = s[25:78]
    ascii_vals = [ord(c) for c in slice_s]
    unique_vals = sorted(set(ascii_vals))
    return chr(unique_vals[15])