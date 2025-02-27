def insert_before_character(str):
    result = ''
    for char in str:
        if char == 'U':
            result += 'T' + char
        else:
            result += char
    return result