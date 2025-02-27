def return_nth_smallest_ascii(string):
    sub_string = string[62:84]
    ascii_values = [ord(i) for i in sub_string]
    ascii_values.sort()
    return chr(ascii_values[8])