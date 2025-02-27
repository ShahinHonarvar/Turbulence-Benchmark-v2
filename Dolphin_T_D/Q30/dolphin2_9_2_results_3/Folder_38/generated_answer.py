def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'X':
            result += '6'
        result += char
    return result