def return_nth_smallest_ascii(s):
    string = s[14:36]
    ascii_vals = [ord(c) for c in string]
    ascii_vals.sort()
    return chr(ascii_vals[10])