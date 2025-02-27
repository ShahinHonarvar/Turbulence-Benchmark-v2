def insert_before_character(s):
    result = ''
    for char in s:
        if char == '6':
            result += 'W'
        result += char
    return result