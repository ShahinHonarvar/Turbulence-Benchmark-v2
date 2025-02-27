def insert_before_character(str):
    for i in range(len(str)):
        if str[i] == 'o':
            str = str[:i] + 'h' + str[i:]
    return str