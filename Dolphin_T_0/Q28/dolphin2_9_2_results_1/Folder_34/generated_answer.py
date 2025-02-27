def return_nth_smallest_ascii(s):
    chars = s[0:19]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    return chr(ascii_vals[18]) if len(ascii_vals) > 18 else 'No character found'