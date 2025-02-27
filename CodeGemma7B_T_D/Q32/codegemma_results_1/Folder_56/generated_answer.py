def insert_after_character(str):
    result = ''
    for char in str:
        result += char
        if char == 'I':
            result += 'i'
    return result