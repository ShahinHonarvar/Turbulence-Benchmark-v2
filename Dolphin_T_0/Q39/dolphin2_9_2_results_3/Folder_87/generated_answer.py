def return_n_greatest_chars(input_string):
    ascii_list = [ord(c) for c in input_string]
    ascii_list_sorted = sorted(ascii_list, reverse=True)[:24]
    output_chars = [chr(i) for i in ascii_list_sorted]
    output_chars_sorted = sorted(output_chars)
    return output_chars_sorted