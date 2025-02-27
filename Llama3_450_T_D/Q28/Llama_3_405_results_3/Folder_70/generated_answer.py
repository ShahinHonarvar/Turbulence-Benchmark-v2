def return_nth_smallest_ascii(s):
    sliced_string = s[28:55]
    ascii_values = [ord(c) for c in sliced_string]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_value = sorted_ascii_values[13]
    return chr(nth_smallest_value)