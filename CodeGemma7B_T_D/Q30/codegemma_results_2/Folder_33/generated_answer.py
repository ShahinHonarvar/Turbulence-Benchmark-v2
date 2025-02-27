def insert_before_character(str):
    for i in range(len(str)):
        if str[i] == 'a':
            str = str[:i] + 'n' + str[i:]
    return str