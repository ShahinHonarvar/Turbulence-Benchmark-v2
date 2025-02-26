def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == 'e':
            result += '0'
    return result