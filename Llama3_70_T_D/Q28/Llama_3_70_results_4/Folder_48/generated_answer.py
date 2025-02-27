def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(37, 60)]
    ascii_values = [(c, ord(c)) for c in chars_in_range]
    sorted_ascii_values = sorted(ascii_values, key=lambda x: x[1])
    return sorted_ascii_values[5][0]