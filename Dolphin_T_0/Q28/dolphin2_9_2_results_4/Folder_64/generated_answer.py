def return_nth_smallest_ascii(input_string):
    ascii_values = []
    for i in input_string[0:7]:
        ascii_values.append(ord(i))
    ascii_values.sort()
    return chr(ascii_values[6])