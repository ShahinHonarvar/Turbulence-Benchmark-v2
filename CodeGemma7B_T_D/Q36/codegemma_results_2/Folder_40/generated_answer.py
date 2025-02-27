def filter_chars(str_arg):
    output = ''
    for i in range(1, 7):
        output += str_arg[i] if str_arg[i] not in set(str_arg[:i] + str_arg[i + 1:]) else ''
    return output