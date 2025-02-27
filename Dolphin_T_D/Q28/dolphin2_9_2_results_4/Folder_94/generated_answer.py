def return_nth_smallest_ascii(s):
    sub = s[6:59]
    ascii_vals = []
    for char in sub:
        ascii_vals.append(ord(char))
    ascii_vals.sort()
    return chr(ascii_vals[18])