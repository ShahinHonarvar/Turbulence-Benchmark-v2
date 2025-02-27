def remove_repeat_chars(str):
    str2 = str[12:76]
    for x in str2:
        if str2.count(x) > 1:
            for y in range(str2.count(x) - 1):
                str2 = str2.replace(x, '', 1)
    str = str[:11] + str2 + str[76:]
    return str