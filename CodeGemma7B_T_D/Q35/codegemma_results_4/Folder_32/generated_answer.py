def remove_repeat_chars(str):
    for i in range(86, 90):
        if str[i] == str[i + 1]:
            str = str[:i] + str[i + 1:]
    return str