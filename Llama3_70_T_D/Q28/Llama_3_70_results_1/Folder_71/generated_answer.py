def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(5, 83)]
    ascii_values = [ord(c) for c in chars_in_range]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii_values[15]
    return chr(nth_smallest_ascii)