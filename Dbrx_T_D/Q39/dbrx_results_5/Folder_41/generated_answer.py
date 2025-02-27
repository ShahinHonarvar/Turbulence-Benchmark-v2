def return_n_greatest_chars(input_string):
    ascii_list = [ord(char) for char in input_string]
    sorted_ascii_list = sorted(ascii_list)[-37:]
    result = [chr(ascii) for ascii in sorted_ascii_list]
    return result