def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'U':
            result += char + 'u'
        else:
            result += char
    return result