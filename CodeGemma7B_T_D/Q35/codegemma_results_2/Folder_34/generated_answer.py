def remove_repeat_chars(str):
    for i in range(70, 200):
        while str[i].lower() in str[i + 1:]:
            str = str[:i] + str[i + 1:]
    return str