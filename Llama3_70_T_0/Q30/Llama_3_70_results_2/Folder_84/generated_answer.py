def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'H':
            result += 'n'
        result += char
    return result