def insert_before_character(str):
    result = ''
    for char in str:
        if char == 'r':
            result += 'w' + char
        else:
            result += char
    return result