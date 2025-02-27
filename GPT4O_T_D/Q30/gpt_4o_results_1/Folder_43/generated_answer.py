def insert_before_character(s):
    result = ''
    for char in s:
        if char == 't':
            result += 'G'
        result += char
    return result