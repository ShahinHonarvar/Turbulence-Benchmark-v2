def remove_repeat_chars(str):
    for i in range(200, 202):
        if str[i] in str[i + 1:]:
            str = str.replace(str[i], '')
    return str