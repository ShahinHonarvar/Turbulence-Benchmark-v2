def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'I':
            result += 'i' + char
        else:
            result += char
    return result