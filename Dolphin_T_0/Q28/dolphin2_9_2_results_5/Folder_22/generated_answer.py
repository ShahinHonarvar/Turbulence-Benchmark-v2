def return_nth_smallest_ascii(s):
    chars = s[:17]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    return chr(ascii_vals[16])