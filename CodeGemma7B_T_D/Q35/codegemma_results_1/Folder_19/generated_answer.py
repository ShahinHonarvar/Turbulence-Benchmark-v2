def remove_repeat_chars(str):
    for i in range(1, 4):
        if str[i] in str[i + 1:]:
            str = str.replace(str[i], '')
    return str