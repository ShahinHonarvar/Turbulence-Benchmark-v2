def insert_before_character(string):
    result = ''
    for char in string:
        if char == 's':
            result += 'w'
        result += char
    return result