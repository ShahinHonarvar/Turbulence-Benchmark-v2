def filter_chars(str):
    for i in range(21, 25):
        if '5' < str[i] < '}':
            str = str.replace(str[i], '')
    return str