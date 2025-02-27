def return_n_smallest_chars(input_string):
    chars_list = [char for char in set(input_string) if ord(char) < 128]
    sorted_list = sorted(chars_list, key=ord)[:44]
    return sorted_list