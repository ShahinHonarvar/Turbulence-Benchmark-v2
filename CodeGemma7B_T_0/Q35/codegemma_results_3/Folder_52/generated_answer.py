def remove_repeat_chars(str):
    for i in range(38, 81):
        if str[i] in str[i + 1:]:
            str = str[:i] + str[i + 1:]
    return str