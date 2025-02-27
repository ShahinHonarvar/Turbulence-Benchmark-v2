def insert_before_character(str):
    str = list(str)
    for i in range(len(str)):
        if str[i] == 'T' and str[i - 1] != 'V':
            str.insert(i, 'V')
            i += 1
    return ''.join(str)