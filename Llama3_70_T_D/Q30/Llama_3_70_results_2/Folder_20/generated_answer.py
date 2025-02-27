def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'C':
            result += 'H'
        result += char
    return result