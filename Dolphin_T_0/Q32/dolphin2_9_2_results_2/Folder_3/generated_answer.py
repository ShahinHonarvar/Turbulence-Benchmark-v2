def insert_after_character(string):
    result = ''
    for i in range(len(string)):
        if string[i] == '0':
            result += string[i] + 'H'
        else:
            result += string[i]
    return result