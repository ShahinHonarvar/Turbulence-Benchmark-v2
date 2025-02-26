def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'e':
            result += '0e'
        else:
            result += char
    return result