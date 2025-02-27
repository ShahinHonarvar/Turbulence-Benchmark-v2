def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'B':
            result += 'N'
        result += char
    return result