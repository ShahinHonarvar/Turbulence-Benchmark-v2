def insert_before_character(string):
    string_list = list(string)
    for i in range(len(string_list) - 1):
        if string_list[i + 1] == 'B':
            string_list.insert(i + 1, 'N')
    return ''.join(string_list)