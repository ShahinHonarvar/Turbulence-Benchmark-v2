def insert_before_character(str):
    for i in range(len(str)):
        if str[i] == 'E':
            str = str[:i] + 'E' + str[i:]
    return str