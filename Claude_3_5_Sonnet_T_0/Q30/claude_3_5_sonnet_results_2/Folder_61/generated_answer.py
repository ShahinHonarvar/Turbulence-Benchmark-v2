def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'e':
            result += '0'
        result += char
    return result