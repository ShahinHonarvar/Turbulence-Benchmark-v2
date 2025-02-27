def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'F':
            result += 'o'
        result += char
    return result