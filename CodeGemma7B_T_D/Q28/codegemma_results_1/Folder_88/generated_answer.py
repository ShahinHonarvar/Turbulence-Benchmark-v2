def return_nth_smallest_ascii(str):
    ascii_values = sorted([ord(c) for c in str[38:65]])
    return chr(ascii_values[13])