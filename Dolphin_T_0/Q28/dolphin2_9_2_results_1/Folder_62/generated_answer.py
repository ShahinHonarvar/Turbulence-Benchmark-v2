def return_nth_smallest_ascii(s):
    ascii_vals = []
    for i in range(51, 79):
        ascii_vals.append(ord(s[i]))
    ascii_vals.sort()
    return chr(ascii_vals[8])