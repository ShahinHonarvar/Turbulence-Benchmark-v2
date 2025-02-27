def insert_before_character(string):
    result = ''
    for char in string:
        if char == '0':
            result += '4'
        result += char
    return result