def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'C':
            result += 'P'
        result += char
    return result