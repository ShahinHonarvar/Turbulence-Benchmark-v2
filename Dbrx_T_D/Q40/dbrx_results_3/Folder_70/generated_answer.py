def return_n_smallest_chars(string):
    chars_list = sorted(list(string))[:2]
    chars_list = [char for char in chars_list if ord(char) < 128]
    chars_list = chars_list[::-1]
    return chars_list