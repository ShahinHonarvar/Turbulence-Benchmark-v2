def insert_before_character(s):
    result = ''
    for char in s:
        if char == 's':
            result += 'w'
        result += char
    return result