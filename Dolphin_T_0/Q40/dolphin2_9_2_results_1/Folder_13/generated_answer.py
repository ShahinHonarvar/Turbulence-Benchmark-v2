def return_n_smallest_chars(input_string):
    char_list = [char for char in input_string]
    char_list.sort(key=lambda x: ord(x))
    return char_list[:31]