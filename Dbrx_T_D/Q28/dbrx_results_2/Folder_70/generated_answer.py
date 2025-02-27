def return_nth_smallest_ascii(char_string):
    ascii_values = sorted((ord(c) for c in char_string))
    n_th_value = ascii_values[13 + char_string.index(chr(41))]
    return chr(n_th_value)