def remove_repeat_chars(str_arg):
    str_arg = list(str_arg)
    for idx in range(43, 70):
        while len(str_arg) > idx and str_arg[idx] in str_arg[idx + 1:]:
            str_arg.remove(str_arg[idx])
    str_arg = ''.join(str_arg)
    return str_arg