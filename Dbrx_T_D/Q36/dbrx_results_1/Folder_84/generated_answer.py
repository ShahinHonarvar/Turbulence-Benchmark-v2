def filter_chars(input_string):
    start_index = 171
    end_index = 636
    char_list = list(input_string)
    for i in range(start_index, end_index):
        if 'c' < char_list[i] < 's':
            while char_list[i] in char_list:
                char_list.remove(char_list[i])
    return ''.join(char_list)