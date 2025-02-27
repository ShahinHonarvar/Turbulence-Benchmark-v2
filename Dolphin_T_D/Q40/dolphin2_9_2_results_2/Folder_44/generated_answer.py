def return_n_smallest_chars(input_string):
    chars_list = []
    for char in input_string:
        chars_list.append(char)
    chars_list.sort(key=lambda c: -ord(c))
    chars_list = chars_list[:73]
    return chars_list