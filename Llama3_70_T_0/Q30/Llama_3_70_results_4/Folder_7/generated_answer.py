def insert_before_character(s):
    result = ''
    for char in s:
        if char == ' ':
            result += 'H'
        result += char
    return result