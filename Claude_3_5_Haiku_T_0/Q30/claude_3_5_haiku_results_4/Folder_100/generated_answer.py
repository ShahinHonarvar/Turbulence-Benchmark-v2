def insert_before_character(s):
    result = ''
    for char in s:
        if char == '0':
            result += ' 0'
        else:
            result += char
    return result