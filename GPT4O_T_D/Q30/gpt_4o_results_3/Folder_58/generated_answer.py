def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'F':
            result += 'oF'
        else:
            result += char
    return result