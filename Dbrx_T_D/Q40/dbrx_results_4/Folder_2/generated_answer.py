def return_n_smallest_chars(input_string):
    ascii_list = [ord(char) for char in input_string]
    ascii_list.sort()
    return [chr(char) for char in ascii_list[:48]]