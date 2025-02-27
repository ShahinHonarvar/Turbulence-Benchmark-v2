def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 48 <= i <= 76]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    if len(ascii_vals) < 5:
        return None
    else:
        return chr(ascii_vals[4])