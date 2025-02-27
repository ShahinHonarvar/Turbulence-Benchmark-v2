def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'x':
            result = result + 'N' + char
        else:
            result = result + char
    return result