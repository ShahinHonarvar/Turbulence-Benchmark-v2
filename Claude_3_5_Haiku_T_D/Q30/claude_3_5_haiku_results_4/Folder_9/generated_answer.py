def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'e':
            result += 'E' + char
        else:
            result += char
    return result