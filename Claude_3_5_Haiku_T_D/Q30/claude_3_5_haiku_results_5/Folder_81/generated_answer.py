def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'A':
            result += 'A'
        result += char
    return result