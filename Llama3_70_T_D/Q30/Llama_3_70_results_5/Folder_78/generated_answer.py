def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'H':
            result += 's'
        result += char
    return result