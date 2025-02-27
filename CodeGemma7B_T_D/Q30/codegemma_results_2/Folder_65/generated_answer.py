def insert_before_character(string):
    result = ''
    for char in string:
        if char == '6':
            result += '9' + char
        else:
            result += char
    return result