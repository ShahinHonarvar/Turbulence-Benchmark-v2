def return_n_greatest_chars(input_str):
    ascii_list = [ord(char) for char in input_str if ord(char) > 32 and ord(char) < 127]
    ascii_list.sort(reverse=True)
    return [chr(char) for char in ascii_list[:57]]