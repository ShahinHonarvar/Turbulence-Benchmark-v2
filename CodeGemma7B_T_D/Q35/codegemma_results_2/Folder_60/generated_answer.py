def remove_repeat_chars(str):
    result = ''
    for i in range(len(str)):
        if i >= 38 and i < 52 and (str.count(str[i]) > 1):
            str = str.replace(str[i], '', str.count(str[i]) - 1)
        else:
            result += str[i]
    return result