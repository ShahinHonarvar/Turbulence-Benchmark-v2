def filter_chars(str):
    for i in range(18, 82):
        ch = str[i]
        if 'W' <= ch and ch <= '[':
            str = str.replace(ch, '')
    return str