def remove_repeat_chars(str):
    for i in range(len(str)):
        if i >= 0 and i <= 6 and (str[i] in str[i + 1:]):
            str = str[:i] + str[i + 1:]
    return str