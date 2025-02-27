def insert_after_character(str):
    result = ''
    for char in str:
        if char == 't':
            result += char + 'u'
        else:
            result += char
    return result