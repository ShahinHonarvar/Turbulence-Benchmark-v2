def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'a':
            result += 'W'
        result += char
    return result