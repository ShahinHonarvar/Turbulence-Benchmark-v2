def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'C':
            result += 'P'
        result += char
    return result