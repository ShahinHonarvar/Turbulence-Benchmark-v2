def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'T':
            result += ' '
        result += char
    return result