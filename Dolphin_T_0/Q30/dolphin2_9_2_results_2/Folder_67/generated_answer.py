def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'j':
            result += '1'
        result += c
    return result