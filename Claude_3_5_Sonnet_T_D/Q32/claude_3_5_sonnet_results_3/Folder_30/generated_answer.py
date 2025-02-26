def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == '4':
            result += 'F'
    return result