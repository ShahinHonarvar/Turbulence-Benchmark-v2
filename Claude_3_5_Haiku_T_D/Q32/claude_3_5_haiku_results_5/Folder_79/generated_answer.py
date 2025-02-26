def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == 'E':
            result += 'E'
    return result