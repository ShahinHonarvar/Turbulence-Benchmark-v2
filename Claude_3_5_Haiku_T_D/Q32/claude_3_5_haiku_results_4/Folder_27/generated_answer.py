def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == 'N':
            result += 'j'
    return result