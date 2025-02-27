def insert_before_character(str):
    for i in range(len(str)):
        if str[i] == 'e':
            str = str[:i] + 'e' + str[i:]
    return str