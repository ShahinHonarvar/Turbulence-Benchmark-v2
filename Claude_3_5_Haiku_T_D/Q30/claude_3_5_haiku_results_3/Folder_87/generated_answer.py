def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'm':
            result += 'Nm'
        else:
            result += char
    return result