def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'R':
            result += 'V'
        result += char
    return result