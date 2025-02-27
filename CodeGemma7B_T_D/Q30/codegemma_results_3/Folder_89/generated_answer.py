def insert_before_character(string):
    result = ''
    for char in string:
        if char == ' ':
            result += 'W '
        else:
            result += char
    return result