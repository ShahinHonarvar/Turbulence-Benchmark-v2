def insert_before_character(string):
    result = ''
    for char in string:
        if char == '5':
            result += 'h'
        result += char
    return result