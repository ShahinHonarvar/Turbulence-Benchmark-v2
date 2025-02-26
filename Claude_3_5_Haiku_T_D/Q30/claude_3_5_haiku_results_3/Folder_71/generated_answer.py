def insert_before_character(string):
    result = ''
    for char in string:
        if char == '2':
            result += 'S2'
        else:
            result += char
    return result