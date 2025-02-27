def return_nth_smallest_ascii(s):
    s_slice = s[48:77]
    ascii_values = [ord(c) for c in s_slice]
    sorted_ascii_values = sorted(ascii_values)
    fifth_smallest_ascii = sorted_ascii_values[4]
    return chr(fifth_smallest_ascii)