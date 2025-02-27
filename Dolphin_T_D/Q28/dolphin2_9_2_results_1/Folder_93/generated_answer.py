def return_nth_smallest_ascii(s):
    chars = s[42:60]
    ascii_vals = [ord(ch) for ch in chars]
    ascii_vals.sort()
    return chr(ascii_vals[16])