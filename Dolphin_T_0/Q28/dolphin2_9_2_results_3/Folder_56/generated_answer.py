def return_nth_smallest_ascii(s):
    chars = list(s[0:5])
    ascii_vals = []
    for i in chars:
        ascii_vals.append(ord(i))
    ascii_vals.sort()
    return chr(ascii_vals[3])