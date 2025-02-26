def insert_before_character(s):
    result = ''
    for char in s:
        if char == '4':
            result += 'F4'
        else:
            result += char
    return result