def return_n_greatest_chars(input_string):
    chars_list = list(input_string)
    chars_list = sorted(set(chars_list))
    chars_list = [char for char in chars_list if ord(char) >= ord(input_string[-40])]
    chars_list = chars_list[-40:]
    return chars_list