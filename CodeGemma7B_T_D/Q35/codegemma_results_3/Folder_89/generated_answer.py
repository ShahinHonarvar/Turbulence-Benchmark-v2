def remove_repeat_chars(str):
    for i in range(55, 84):
        if str[i] in str[i + 1:84]:
            str = str.replace(str[i], '')
    return str