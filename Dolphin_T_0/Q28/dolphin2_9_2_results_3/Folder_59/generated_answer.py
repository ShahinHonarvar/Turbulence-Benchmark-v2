def return_nth_smallest_ascii(s: str):
    ascii_vals = [ord(c) for c in s[:12]]
    ascii_vals.sort()
    return chr(ascii_vals[11])