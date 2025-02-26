def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'E':
            result += 'E'
        result += char
    return result