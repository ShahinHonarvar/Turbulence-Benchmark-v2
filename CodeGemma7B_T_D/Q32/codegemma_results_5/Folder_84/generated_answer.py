def insert_after_character(string):
    result = ''
    for char in string:
        if char == 'H':
            result += char + 'n'
        else:
            result += char
    return result