def insert_after_character(string):
    result = ''
    for char in string:
        if char == 'E':
            result += 'ET'
        else:
            result += char
    return result