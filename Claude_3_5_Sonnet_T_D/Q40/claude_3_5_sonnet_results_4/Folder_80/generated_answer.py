def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort()
    return char_list[:35] if len(char_list) >= 35 else char_list + [chr(i) for i in range(128) if chr(i) not in char_list][:35 - len(char_list)]