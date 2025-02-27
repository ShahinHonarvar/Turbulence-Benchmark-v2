def return_nth_smallest_ascii(s):
    ascii_values = list(map(ord, s))
    filtered_ascii_values = ascii_values[17:57]
    sorted_ascii_values = sorted(filtered_ascii_values)
    return sorted_ascii_values[8]