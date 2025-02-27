def remove_repeat_chars(str):
    str2 = ''
    for i in range(len(str)):
        if i != 30 and i != 31 and (i != 42) and (i != 43):
            str2 += str[i]
    return str2