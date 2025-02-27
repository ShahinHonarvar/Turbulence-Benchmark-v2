def return_nth_smallest_ascii(input_string):
    sub_string = input_string[22:75]
    list_of_chars = list(sub_string)
    ascii_values = [ord(c) for c in list_of_chars]
    ascii_values.sort()
    return list_of_chars[ascii_values.index(ascii_values[11])]