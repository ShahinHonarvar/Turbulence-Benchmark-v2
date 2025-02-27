def insert_before_character(string):
    result = ''
    for char in string:
        if char == '6':
            result += 'W'
        result += char
    return result