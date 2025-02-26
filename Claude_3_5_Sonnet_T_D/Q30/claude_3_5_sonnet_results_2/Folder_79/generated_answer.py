def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'E':
            result += 'E'
        result += char
    return result