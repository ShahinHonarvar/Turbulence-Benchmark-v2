def filter_chars(str):
    for i in range(21, 44):
        while str[i] >= '+' and str[i] <= '8':
            str = str[:i] + str[i + 1:]
    return str