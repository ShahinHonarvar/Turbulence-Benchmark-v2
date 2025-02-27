def insert_after_character(my_string):
    my_list = list(my_string)
    for i in range(len(my_list)):
        if my_list[i] == 'g':
            my_list.insert(i + 1, 't')
            i += 1
    return ''.join(my_list)