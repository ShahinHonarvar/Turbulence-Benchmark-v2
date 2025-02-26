def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'O':
            result += 'd'
        result += char
    return result