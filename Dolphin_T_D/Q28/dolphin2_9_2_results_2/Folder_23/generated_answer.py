def return_nth_smallest_ascii(s):
    ascii_vals = [ord(c) for c in s[29:48] if c in s[29:48]]
    ascii_vals.sort()
    return chr(ascii_vals[7])