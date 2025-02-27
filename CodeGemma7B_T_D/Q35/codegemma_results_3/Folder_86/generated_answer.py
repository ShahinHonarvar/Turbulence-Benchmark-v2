def remove_repeat_chars(str_arg):
    for i in range(19, 32):
        while str_arg[i] in str_arg[i + 1:32]:
            str_arg = str_arg[:i] + str_arg[i + 1:]
    return str_arg