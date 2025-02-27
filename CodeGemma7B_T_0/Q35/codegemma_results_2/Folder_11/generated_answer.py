def remove_repeat_chars(str):
    for i in range(48, 76):
        if str[i] in str[i + 1:]:
            str = str[:i] + str[i + 1:]
    return str