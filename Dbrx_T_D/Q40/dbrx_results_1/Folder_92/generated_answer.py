def return_n_smallest_chars(input_string):
    input_list = [char for char in set(input_string) if input_string.count(char) == 1]
    input_list.sort(key=lambda char: ord(char))
    return input_list[-63:]