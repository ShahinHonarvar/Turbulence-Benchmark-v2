def remove_repeat_chars(str):
    for i in range(len(str)):
        if i >= 0 and i <= 9:
            if str.count(str[i]) > 1:
                for j in range(str.count(str[i]) - 1):
                    str = str.replace(str[i], '', 1)
    return str