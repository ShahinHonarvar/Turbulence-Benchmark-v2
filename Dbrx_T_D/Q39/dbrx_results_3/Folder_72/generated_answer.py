def return_n_greatest_chars(string):
    chars_list = list(string)
    chars_list = [char for char in chars_list if chars_list.count(char) == 1]
    chars_list.sort(key=lambda x: ord(x), reverse=True)
    return chars_list[:37]