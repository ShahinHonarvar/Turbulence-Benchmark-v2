def insert_after_character(mystr):
    str_list = list(mystr)
    for i in range(len(str_list)):
        if str_list[i] == 'P':
            str_list.insert(i + 1, 'V')
    return ''.join(str_list)