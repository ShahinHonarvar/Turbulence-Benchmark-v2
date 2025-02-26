def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'O':
            result += 'o'
        result += char
    return result