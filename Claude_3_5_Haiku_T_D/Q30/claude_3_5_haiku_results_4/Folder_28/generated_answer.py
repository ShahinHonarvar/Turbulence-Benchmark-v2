def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'r':
            result += '1r'
        else:
            result += char
    return result