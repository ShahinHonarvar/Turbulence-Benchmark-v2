def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'a':
            result += 'n'
        result += char
    return result