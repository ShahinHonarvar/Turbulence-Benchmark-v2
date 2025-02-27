def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'S':
            result += 'U'
        result += char
    return result