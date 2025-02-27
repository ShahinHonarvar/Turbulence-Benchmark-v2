def filter_chars(str):
    for i in range(70, 74):
        if str[i] in range('A', 'U'):
            str = str[:i] + str[i + 1:]
            i -= 1
    return str