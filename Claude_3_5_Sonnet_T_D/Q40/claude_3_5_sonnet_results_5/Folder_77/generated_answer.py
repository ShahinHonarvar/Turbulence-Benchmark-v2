def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort()
    return char_list[:47] if len(char_list) >= 47 else char_list + [chr(i) for i in range(128) if chr(i) not in char_list][:47 - len(char_list)]