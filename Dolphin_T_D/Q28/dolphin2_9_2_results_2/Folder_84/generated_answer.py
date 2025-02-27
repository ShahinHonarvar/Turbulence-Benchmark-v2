def return_nth_smallest_ascii(s):
    sub_s = s[52:80]
    ascii_vals = [ord(ch) for ch in sub_s]
    return chr(ascii_vals[6])