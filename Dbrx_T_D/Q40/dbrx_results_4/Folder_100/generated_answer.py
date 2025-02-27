def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    sorted_ascii_values = sorted(ascii_values)[:72]
    sorted_chars = sorted(input_string, key=input_string.index)[:72]
    result = [char for char in sorted_chars if ord(char) in sorted_ascii_values]
    return result[::-1]