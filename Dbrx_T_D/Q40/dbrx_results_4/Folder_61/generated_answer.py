def return_n_smallest_chars(input_string):
    ascii_list = [ord(char) for char in input_string]
    ascii_list.sort(reverse=True)
    result = [chr(item) for item in ascii_list[:66]]
    return result