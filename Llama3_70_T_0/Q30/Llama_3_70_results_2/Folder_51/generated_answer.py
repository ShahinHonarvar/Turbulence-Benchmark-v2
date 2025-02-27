def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'o':
            result += 'O'
        result += char
    return result