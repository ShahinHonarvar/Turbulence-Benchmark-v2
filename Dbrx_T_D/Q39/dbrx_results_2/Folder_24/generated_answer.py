def return_n_greatest_chars(string):
    chars_list = [char for char in string if char != ' ']
    chars_list.sort(key=lambda char: ord(char), reverse=True)
    return chars_list[:32]