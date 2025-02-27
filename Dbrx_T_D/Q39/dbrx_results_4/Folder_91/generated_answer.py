def return_n_greatest_chars(input_str):
    ascii_list = [ord(char) for char in input_str]
    ascii_list.sort(reverse=True)
    return [chr(char) for char in ascii_list[:6]]