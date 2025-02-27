def return_nth_smallest_ascii(s):
    sub = s[13:36]
    ascii_vals = [ord(c) for c in sub]
    nth_smallest_ascii = sorted(ascii_vals)[17]
    return chr(nth_smallest_ascii)