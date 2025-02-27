import string

def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string]
    ascii_values_63_76 = ascii_values[63:77]
    sorted_ascii_values = sorted(ascii_values_63_76)
    return chr(sorted_ascii_values[13])