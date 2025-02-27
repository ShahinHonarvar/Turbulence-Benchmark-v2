def insert_after_character(a):
    result = ''
    for char in a:
        if char == 'O':
            result += char + 'Q'
        else:
            result += char
    return result