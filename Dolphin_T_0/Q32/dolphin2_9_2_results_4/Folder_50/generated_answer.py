def insert_after_character(string):
    result = ''
    for i in range(len(string)):
        result += string[i]
        if string[i:i + 1] == 't':
            result += 'u'
    return result