def remove_repeat_chars(str):
    for i in range(17, 88):
        if str.count(str[i]) > 1 and str[i] != ' ':
            str = str.replace(str[i], '')
    return str