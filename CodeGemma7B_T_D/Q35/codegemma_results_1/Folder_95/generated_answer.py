def remove_repeat_chars(str):
    for i in range(32, 99):
        if str[i] in str[:i]:
            str = str.replace(str[i], '')
    return str