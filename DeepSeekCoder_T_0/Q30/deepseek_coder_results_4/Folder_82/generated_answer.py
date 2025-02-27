def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'I':
            result += 'I'
        result += char
    return result