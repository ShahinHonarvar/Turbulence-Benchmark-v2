def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == 'm':
            result += 'Q'
    return result