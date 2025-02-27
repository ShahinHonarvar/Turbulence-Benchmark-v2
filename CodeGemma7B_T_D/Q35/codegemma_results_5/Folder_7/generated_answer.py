def remove_repeat_chars(str):
    for i in range(375, 926):
        if str[i] in str[i + 1:]:
            str = str.replace(str[i], '')
    return str