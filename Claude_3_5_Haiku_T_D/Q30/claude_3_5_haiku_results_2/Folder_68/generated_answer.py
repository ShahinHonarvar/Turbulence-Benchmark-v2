def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'i':
            result += '0i'
        else:
            result += char
    return result