def return_nth_smallest_ascii(s):
    s = s[5:83]
    ascii_values = [ord(c) for c in s]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii_values[15]
    nth_smallest_char = chr(nth_smallest_ascii)
    return nth_smallest_char