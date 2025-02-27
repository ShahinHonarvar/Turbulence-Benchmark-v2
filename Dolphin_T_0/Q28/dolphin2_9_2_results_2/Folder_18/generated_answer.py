def return_nth_smallest_ascii(input_string):
    filtered_string = input_string[51:61]
    ascii_values = [ord(c) for c in filtered_string]
    ascii_values.sort()
    return filtered_string[ascii_values.index(ascii_values[4])]