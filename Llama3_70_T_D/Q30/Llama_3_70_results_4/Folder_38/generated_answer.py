def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'X':
            result += '6'
        result += char
    return result