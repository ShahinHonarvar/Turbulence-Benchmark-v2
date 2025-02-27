def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'a':
            result += '6' + char
        else:
            result += char
    return result