def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == ' ':
            result += '5'
    return result