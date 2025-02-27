def insert_before_character(str):
    result = ''
    for char in str:
        if char == 'e':
            result += 'W' + char
        else:
            result += char
    return result