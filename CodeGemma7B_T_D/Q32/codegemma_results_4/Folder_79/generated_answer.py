def insert_after_character(str):
    result = ''
    for char in str:
        if char == 'E':
            result += 'E'
        result += char
    return result