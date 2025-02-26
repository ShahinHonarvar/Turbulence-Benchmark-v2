def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == 'X':
            result += 'u'
    return result