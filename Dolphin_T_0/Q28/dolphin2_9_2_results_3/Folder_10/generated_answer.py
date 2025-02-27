def return_nth_smallest_ascii(s):
    ascii_vals = [ord(c) for c in s[38:83]]
    ascii_vals.sort()
    return chr(ascii_vals[19])