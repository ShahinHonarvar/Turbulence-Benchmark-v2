def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'o':
            result += 'O' + char
        else:
            result += char
    return result