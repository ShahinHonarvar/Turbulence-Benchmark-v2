def insert_after_character(string):
    string_list = list(string)
    for i in range(len(string_list)):
        if string_list[i] == '5':
            string_list.insert(i + 1, 'h')
    return ''.join(string_list)