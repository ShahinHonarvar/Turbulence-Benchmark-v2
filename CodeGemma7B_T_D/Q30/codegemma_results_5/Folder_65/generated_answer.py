def insert_before_character(str):
    for i in range(len(str)):
        if str[i] == '6':
            return str[:i] + '9' + str[i:]
    if str[-1] == '6':
        return str + '9'