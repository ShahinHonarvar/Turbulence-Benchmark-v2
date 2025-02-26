def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == '6':
            result += 'W'
    return result