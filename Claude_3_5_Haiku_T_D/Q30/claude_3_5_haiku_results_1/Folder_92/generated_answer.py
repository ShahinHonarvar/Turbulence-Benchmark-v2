def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'a':
            result += 'a'
        result += char
    return result