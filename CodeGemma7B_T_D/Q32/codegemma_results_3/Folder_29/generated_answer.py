def insert_after_character(str):
    result = ''
    for char in str:
        if char == 'N':
            result += char + 'z'
        else:
            result += char
    return result