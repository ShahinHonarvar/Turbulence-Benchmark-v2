def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'K':
            result += 'l'
        result += char
    return result