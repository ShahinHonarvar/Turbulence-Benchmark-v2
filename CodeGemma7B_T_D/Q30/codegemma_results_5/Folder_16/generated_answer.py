def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'w':
            result += 'n' + char
        else:
            result += char
    return result