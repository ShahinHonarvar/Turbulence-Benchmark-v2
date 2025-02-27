def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'E':
            result += 'f'
        result += char
    return result