def filter_chars(str):
    for i in range(344, 874):
        char = str[i]
        if char > 'f' and char < '~':
            str = str.replace(char, '')
    return str