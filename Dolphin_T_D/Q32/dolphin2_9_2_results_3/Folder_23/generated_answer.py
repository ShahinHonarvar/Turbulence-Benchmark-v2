def insert_after_character(s):
    s_list = list(s)
    for i in range(len(s_list) - 1):
        if s_list[i] == 'b':
            s_list.insert(i + 1, 'y')
    return ''.join(s_list)