def return_nth_smallest_ascii(str):
    ascii_values = sorted([ord(c) for c in str[9:83]])
    return chr(ascii_values[17])