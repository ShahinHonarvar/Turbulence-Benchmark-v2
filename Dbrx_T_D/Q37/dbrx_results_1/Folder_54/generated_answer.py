def filter_chars(input_string):
    char_list = list(input_string)
    filtered_list = []
    for i in range(len(char_list)):
        if i < 46 or i > 85 or ord(char_list[i]) < ord('-') or (ord(char_list[i]) > ord('X')):
            filtered_list.append(char_list[i])
    return ''.join(filtered_list)