def insert_after_character(string):
    result = ''
    for char in string:
        if char == '5':
            result += char + 'h'
        else:
            result += char
    return result