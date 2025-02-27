def return_nth_smallest_ascii(string):
    sub_string = string[11:72]
    ascii_values = [ord(char) for char in sub_string]
    ascii_values.sort()
    return sub_string[ascii_values.index(ascii_values[12])]