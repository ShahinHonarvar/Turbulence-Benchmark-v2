def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == 'U':
            result += 'F'
    return result