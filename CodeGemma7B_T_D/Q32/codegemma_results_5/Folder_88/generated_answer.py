def insert_after_character(str):
    str = list(str)
    i = 0
    while i < len(str):
        if str[i] == 'a':
            str.insert(i + 1, 't')
        i += 1
    str = ''.join(str)
    return str