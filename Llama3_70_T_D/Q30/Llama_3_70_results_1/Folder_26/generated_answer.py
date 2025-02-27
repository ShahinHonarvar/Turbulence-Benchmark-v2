def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'r':
            result += 'w'
        result += char
    return result