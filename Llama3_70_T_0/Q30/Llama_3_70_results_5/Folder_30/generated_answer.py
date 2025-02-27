def insert_before_character(s):
    result = ''
    for char in s:
        if char == '4':
            result += 'F'
        result += char
    return result