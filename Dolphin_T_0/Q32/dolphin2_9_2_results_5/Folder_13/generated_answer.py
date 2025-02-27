def insert_after_character(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == 'x':
            s_list.insert(i + 1, 'N')
    return ''.join(s_list)