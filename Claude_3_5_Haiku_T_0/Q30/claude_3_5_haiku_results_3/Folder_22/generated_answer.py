def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'U':
            result += 'U'
        result += char
    return result