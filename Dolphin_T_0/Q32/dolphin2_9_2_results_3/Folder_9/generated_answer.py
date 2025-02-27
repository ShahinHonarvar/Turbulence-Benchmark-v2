def insert_after_character(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == 'e':
            s_list.insert(i + 1, 'E')
    return ''.join(s_list)