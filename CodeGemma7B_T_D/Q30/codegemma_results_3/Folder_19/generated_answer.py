def insert_before_character(arg):
    list_arg = list(arg)
    for i in range(len(list_arg)):
        if list_arg[i] == '5':
            list_arg.insert(i, 'h')
            i += 1
    return ''.join(list_arg)