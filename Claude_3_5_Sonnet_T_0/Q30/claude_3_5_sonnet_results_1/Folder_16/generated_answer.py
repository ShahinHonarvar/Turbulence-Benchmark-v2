def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'w':
            result += 'n'
        result += char
    return result