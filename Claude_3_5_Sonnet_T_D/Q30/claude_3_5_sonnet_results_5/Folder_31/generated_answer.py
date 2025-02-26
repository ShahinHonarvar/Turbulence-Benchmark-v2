def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'B':
            result += 'N'
        result += char
    return result