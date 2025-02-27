def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[14:22]
    ascii_vals = [ord(c) for c in sub_s]
    ascii_vals.sort()
    return chr(ascii_vals[5])