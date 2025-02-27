def insert_after_character(string):
    string_list = list(string)
    for i in range(len(string_list)):
        if string_list[i] == 'o':
            string_list.insert(i + 1, 'a')
    return ''.join(string_list)