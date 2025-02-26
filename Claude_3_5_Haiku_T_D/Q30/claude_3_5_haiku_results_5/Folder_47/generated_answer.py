def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'E':
            result += 'f'
        result += char
    return result