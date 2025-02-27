def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'w':
            result = result + 'n' + char
        else:
            result = result + char
    return result