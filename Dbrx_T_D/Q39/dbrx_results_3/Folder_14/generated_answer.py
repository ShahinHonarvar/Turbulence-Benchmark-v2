def return_n_greatest_chars(string):
    chars_list = list(string)
    chars_list = sorted(chars_list, key=lambda char: ord(char))
    return chars_list[::-1][:69]