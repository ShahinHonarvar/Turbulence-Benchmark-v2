def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'I':
            result += ' '
        result += char
    return result