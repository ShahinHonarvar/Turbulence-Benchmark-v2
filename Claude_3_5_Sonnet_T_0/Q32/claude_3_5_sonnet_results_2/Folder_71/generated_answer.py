def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == '2':
            result += 'S'
    return result