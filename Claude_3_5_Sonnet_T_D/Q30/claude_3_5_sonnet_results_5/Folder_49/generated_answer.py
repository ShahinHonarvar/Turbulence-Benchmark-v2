def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'i':
            result += 'i'
        result += char
    return result