def insert_before_character(word):
    str_list = list(word)
    for i in range(len(str_list)):
        if str_list[i] == 'o':
            str_list.insert(i, 'O')
            i += 1
    return ''.join(str_list)