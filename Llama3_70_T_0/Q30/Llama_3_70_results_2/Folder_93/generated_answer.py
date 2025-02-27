def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'Y':
            result += '4'
        result += char
    return result