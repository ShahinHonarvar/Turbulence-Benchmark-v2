def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'E':
            result += 'T'
        result += char
    return result