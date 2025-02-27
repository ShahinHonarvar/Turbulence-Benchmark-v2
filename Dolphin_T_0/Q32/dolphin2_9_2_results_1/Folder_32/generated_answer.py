def insert_after_character(str):
    result = ''
    for c in str:
        result += c
        if c == 'F':
            result += 'u'
    return result