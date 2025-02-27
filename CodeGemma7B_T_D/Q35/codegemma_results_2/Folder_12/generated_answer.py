def remove_repeat_chars(str):
    for i in range(16, 87):
        if str.count(str[i]) > 1:
            while str[i] in str:
                str = str.replace(str[i], '', 1)
    return str