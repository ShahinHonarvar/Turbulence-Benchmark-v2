def filter_chars(str):
    for i in range(len(str)):
        if i >= 0 and i <= 1 and (str[i] >= '*') and (str[i] <= 's'):
            str = str[:i] + str[i + 1:]
    return str