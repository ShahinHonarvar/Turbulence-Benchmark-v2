def filter_chars(str):
    res = ''
    for i in range(len(str)):
        if not (i >= 15 and i <= 55 and (str[i] >= 'W') and (str[i] <= '}')):
            res += str[i]
    return res