def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'x':
            result += 'N'
        result += char
    return result