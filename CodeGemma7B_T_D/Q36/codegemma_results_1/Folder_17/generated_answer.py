def filter_chars(str):
    for i in range(19, 95):
        char = chr(i)
        if char > 'K' and char < 'a':
            str = str.replace(char, '')
    return str