def insert_before_character(str):
    result = ''
    for i in range(len(str)):
        if str[i] == 'U':
            result += 'aU'
        else:
            result += str[i]
    return result