def remove_repeat_chars(str):
    str = list(str)
    i = 0
    for i in range(len(str)):
        if i > 12 and i < 91 and (str.count(str[i]) > 1):
            str.remove(str[i])
    return ''.join(str)