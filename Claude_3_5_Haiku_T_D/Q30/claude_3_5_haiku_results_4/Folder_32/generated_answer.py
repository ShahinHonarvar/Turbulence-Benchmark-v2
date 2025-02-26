def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'F':
            result += 'u'
        result += char
    return result