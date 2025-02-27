def return_nth_smallest_ascii(s):
    ascii_vals = [ord(c) for c in s[17:84]]
    ascii_vals.sort()
    return chr(ascii_vals[4])