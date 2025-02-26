def insert_before_character(string):
    result = ''
    for char in string:
        if char == '0':
            result += ' '
        result += char
    return result