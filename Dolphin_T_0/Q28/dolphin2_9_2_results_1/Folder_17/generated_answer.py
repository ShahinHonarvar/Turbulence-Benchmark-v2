def return_nth_smallest_ascii(input_string):
    ascii_values = []
    for index in range(4, 34):
        ascii_values.append(ord(input_string[index]))
    ascii_values.sort()
    return chr(ascii_values[3])