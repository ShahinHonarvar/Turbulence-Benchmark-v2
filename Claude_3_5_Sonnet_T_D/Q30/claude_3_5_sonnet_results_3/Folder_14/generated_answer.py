def insert_before_character(s):
    result = ''
    for char in s:
        if char == '.':
            result += ' '
        result += char
    return result