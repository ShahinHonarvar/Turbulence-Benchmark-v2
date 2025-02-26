def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == 'X':
            result += '6'
    return result