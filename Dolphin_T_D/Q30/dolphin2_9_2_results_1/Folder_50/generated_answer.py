def insert_before_character(string):
    result = ''
    for char in string:
        if char == 't':
            result += 'u' + char
        else:
            result += char
    return result