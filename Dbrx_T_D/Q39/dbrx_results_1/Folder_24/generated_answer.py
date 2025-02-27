def return_n_greatest_chars(string):
    chars_list = list(set(string))
    chars_list.sort(reverse=True, key=lambda char: ord(char))
    return chars_list[:32]