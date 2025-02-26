def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'w':
            result += 'n'
        result += char
    return result