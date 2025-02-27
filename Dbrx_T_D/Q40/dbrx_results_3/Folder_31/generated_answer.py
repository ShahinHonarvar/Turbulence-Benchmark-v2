def return_n_smallest_chars(input_str):
    ascii_list = [ord(char) for char in input_str]
    ascii_list.sort(reverse=True)
    n_chars_list = [chr(ascii_val) for ascii_val in ascii_list[:70]]
    return n_chars_list