def return_nth_smallest_ascii(s):
    sliced_string = s[62:84]
    ascii_values = [ord(c) for c in sliced_string]
    sorted_ascii_values = sorted(ascii_values)
    ninth_smallest_value = sorted_ascii_values[8]
    return chr(ninth_smallest_value)